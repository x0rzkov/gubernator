/*
Copyright 2018-2019 Mailgun Technologies Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package gubernator

import (
	"context"
	"encoding/json"

	etcd "github.com/coreos/etcd/clientv3"
	"github.com/mailgun/holster/v3/clock"
	"github.com/mailgun/holster/v3/setter"
	"github.com/mailgun/holster/v3/syncutil"
	"github.com/pkg/errors"
	"github.com/sirupsen/logrus"
)

const (
	etcdTimeout    = clock.Second * 10
	backOffTimeout = clock.Second * 5
	leaseTTL       = 30
	defaultBaseKey = "/gubernator/peers/"
)

type PoolInterface interface {
	Close()
}

type EtcdPool struct {
	peers     map[string]PeerInfo
	wg        syncutil.WaitGroup
	ctx       context.Context
	cancelCtx context.CancelFunc
	watchChan etcd.WatchChan
	log       logrus.FieldLogger
	watcher   etcd.Watcher
	conf      EtcdPoolConfig
}

type EtcdPoolConfig struct {
	// (Required) The address etcd will advertise to other gubernator instances
	AdvertiseAddress string

	// (Required) An etcd client currently connected to an etcd cluster
	Client *etcd.Client

	// (Required) Called when the list of gubernators in the pool updates
	OnUpdate UpdateFunc

	// (Optional) The etcd key prefix used when discovering other peers. Defaults to `/gubernator/peers/`
	KeyPrefix string

	// (Optional) The etcd config used to connect to the etcd cluster
	EtcdConfig *etcd.Config

	// (Optional) An interface through which logging will occur (Usually *logrus.Entry)
	Logger logrus.FieldLogger

	// (Optional) The datacenter this instance belongs too
	DataCenter string
}

func NewEtcdPool(conf EtcdPoolConfig) (*EtcdPool, error) {
	setter.SetDefault(&conf.KeyPrefix, defaultBaseKey)
	setter.SetDefault(&conf.Logger, logrus.WithField("category", "gubernator"))

	if conf.AdvertiseAddress == "" {
		return nil, errors.New("AdvertiseAddress is required")
	}

	if conf.Client == nil {
		return nil, errors.New("Client is required")
	}

	ctx, cancel := context.WithCancel(context.Background())
	pool := &EtcdPool{
		log:       conf.Logger,
		peers:     make(map[string]PeerInfo),
		cancelCtx: cancel,
		conf:      conf,
		ctx:       ctx,
	}
	return pool, pool.run(conf.AdvertiseAddress)
}

func (e *EtcdPool) run(addr string) error {

	// Register our instance with etcd
	if err := e.register(addr); err != nil {
		return err
	}

	// Get our peer list and watch for changes
	if err := e.watch(); err != nil {
		return err
	}
	return nil
}

func (e *EtcdPool) watchPeers() error {
	var revision int64

	// Update our list of peers
	if err := e.collectPeers(&revision); err != nil {
		return err
	}

	// Cancel any previous watches
	if e.watcher != nil {
		e.watcher.Close()
	}

	e.watcher = etcd.NewWatcher(e.conf.Client)

	ready := make(chan struct{})
	go func() {
		e.watchChan = e.watcher.Watch(etcd.WithRequireLeader(e.ctx), e.conf.KeyPrefix,
			etcd.WithRev(revision), etcd.WithPrefix(), etcd.WithPrevKV())
		close(ready)
	}()

	select {
	case <-ready:
		e.log.Infof("watching for peer changes '%s' at revision %d", e.conf.KeyPrefix, revision)
	case <-clock.After(etcdTimeout):
		return errors.New("timed out while waiting for watcher.Watch() to start")
	}
	return nil
}

func (e *EtcdPool) collectPeers(revision *int64) error {
	ctx, cancel := context.WithTimeout(e.ctx, etcdTimeout)
	defer cancel()

	resp, err := e.conf.Client.Get(ctx, e.conf.KeyPrefix, etcd.WithPrefix())
	if err != nil {
		return errors.Wrapf(err, "while fetching peer listing from '%s'", e.conf.KeyPrefix)
	}

	// Collect all the peers
	for _, v := range resp.Kvs {
		p := e.unMarshallValue(v.Value)
		e.peers[p.GRPCAddress] = p
	}

	e.callOnUpdate()
	return nil
}

func (e *EtcdPool) unMarshallValue(v []byte) PeerInfo {
	var p PeerInfo

	// for backward compatible with older gubernator versions
	if err := json.Unmarshal(v, &p); err != nil {
		e.log.WithError(err).Errorf("while unmarshalling peer info from key value")
		return PeerInfo{GRPCAddress: string(v)}
	}
	return p
}

func (e *EtcdPool) watch() error {
	// Initialize watcher
	if err := e.watchPeers(); err != nil {
		return errors.Wrap(err, "while attempting to start watch")
	}

	e.wg.Until(func(done chan struct{}) bool {
		for response := range e.watchChan {
			if response.Canceled {
				e.log.Infof("graceful watch shutdown")
				return false
			}

			if err := response.Err(); err != nil {
				e.log.Errorf("watch error: %v", err)
				goto restart
			}

			for _, event := range response.Events {
				switch event.Type {
				case etcd.EventTypePut:
					if event.Kv != nil {
						e.log.Debugf("new peer [%s]", string(event.Kv.Value))
						p := e.unMarshallValue(event.Kv.Value)
						e.peers[p.GRPCAddress] = p
					}
				case etcd.EventTypeDelete:
					if event.PrevKv != nil {
						e.log.Debugf("removed peer [%s]", string(event.PrevKv.Value))
						delete(e.peers, string(event.PrevKv.Value))
					}
				}
				e.callOnUpdate()
			}
		}

	restart:
		// Are we in the middle of a shutdown?
		select {
		case <-done:
			return false
		case <-e.ctx.Done():
			return false
		default:
		}

		if err := e.watchPeers(); err != nil {
			e.log.WithError(err).
				Error("while attempting to restart watch")
			select {
			case <-clock.After(backOffTimeout):
				return true
			case <-done:
				return false
			}
		}

		return true
	})
	return nil
}

func (e *EtcdPool) register(name string) error {
	instanceKey := e.conf.KeyPrefix + name
	e.log.Infof("Registering peer '%s' with etcd", name)

	b, err := json.Marshal(PeerInfo{
		GRPCAddress: e.conf.AdvertiseAddress,
		DataCenter:  e.conf.DataCenter,
	})
	if err != nil {
		return errors.Wrap(err, "while marshalling PeerInfo")
	}

	var keepAlive <-chan *etcd.LeaseKeepAliveResponse
	var lease *etcd.LeaseGrantResponse

	register := func() error {
		ctx, cancel := context.WithTimeout(e.ctx, etcdTimeout)
		defer cancel()
		var err error

		lease, err = e.conf.Client.Grant(ctx, leaseTTL)
		if err != nil {
			return errors.Wrapf(err, "during grant lease")
		}

		_, err = e.conf.Client.Put(ctx, instanceKey, string(b), etcd.WithLease(lease.ID))
		if err != nil {
			return errors.Wrap(err, "during put")
		}

		if keepAlive, err = e.conf.Client.KeepAlive(e.ctx, lease.ID); err != nil {
			return err
		}
		return nil
	}

	var lastKeepAlive clock.Time

	// Attempt to register our instance with etcd
	if err = register(); err != nil {
		return errors.Wrap(err, "during initial peer registration")
	}

	e.wg.Until(func(done chan struct{}) bool {
		// If we have lost our keep alive, register again
		if keepAlive == nil {
			if err = register(); err != nil {
				e.log.WithError(err).
					Error("while attempting to re-register peer")
				select {
				case <-clock.After(backOffTimeout):
					return true
				case <-done:
					return false
				}
			}
		}

		select {
		case _, ok := <-keepAlive:
			if !ok {
				// Don't re-register if we are in the middle of a shutdown
				if e.ctx.Err() != nil {
					return true
				}

				e.log.Warn("keep alive lost, attempting to re-register peer")
				// re-register
				keepAlive = nil
				return true
			}

			// Ensure we are getting keep alive's regularly
			if lastKeepAlive.Sub(clock.Now()) > clock.Second*leaseTTL {
				e.log.Warn("to long between keep alive heartbeats, re-registering peer")
				keepAlive = nil
				return true
			}
			lastKeepAlive = clock.Now()
		case <-done:
			ctx, cancel := context.WithTimeout(context.Background(), etcdTimeout)
			if _, err := e.conf.Client.Delete(ctx, instanceKey); err != nil {
				e.log.WithError(err).
					Warn("during etcd delete")
			}

			if _, err := e.conf.Client.Revoke(ctx, lease.ID); err != nil {
				e.log.WithError(err).
					Warn("during lease revoke")
			}
			cancel()
			return false
		}
		return true
	})

	return nil
}

func (e *EtcdPool) Close() {
	e.cancelCtx()
	e.wg.Stop()
}

func (e *EtcdPool) callOnUpdate() {
	var peers []PeerInfo

	for _, p := range e.peers {
		if p.GRPCAddress == e.conf.AdvertiseAddress {
			p.IsOwner = true
		}
		peers = append(peers, p)
	}

	e.conf.OnUpdate(peers)
}
