package gubernator_test

import (
	"context"
	"github.com/mailgun/gubernator"
	"github.com/mailgun/gubernator/pb"
	"math/rand"
	"testing"
	"time"
)

func randomString(n int) string {
	const alphanum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	var bytes = make([]byte, n)
	rand.Read(bytes)
	for i, b := range bytes {
		bytes[i] = alphanum[b%byte(len(alphanum))]
	}
	return string(bytes)
}

func BenchmarkServer_GetRateLimitByKey(b *testing.B) {
	client := gubernator.NewPeerClient(gubernator.RandomPeer(peers))

	b.Run("GetPeerRateLimits", func(b *testing.B) {
		for n := 0; n < b.N; n++ {
			_, err := client.GetPeerRateLimits(context.Background(), &pb.RateLimitRequest{
				Namespace: "get_peer_rate_limits_benchmark",
				UniqueKey: randomString(10),
				RateLimitConfig: &pb.RateLimitConfig{
					Limit:    10,
					Duration: 5,
				},
				Hits: 1,
			})
			if err != nil {
				b.Errorf("client.RateLimit() err: %s", err)
			}
		}
	})
}

func BenchmarkServer_GetRateLimit(b *testing.B) {
	client, err := gubernator.NewClient(gubernator.RandomPeer(peers))
	if err != nil {
		b.Errorf("NewClient err: %s", err)
	}

	b.Run("GetRateLimit", func(b *testing.B) {
		for n := 0; n < b.N; n++ {
			_, err := client.GetRateLimit(context.Background(), &gubernator.Request{
				Namespace: "get_rate_limit_benchmark",
				UniqueKey: randomString(10),
				Limit:     10,
				Duration:  time.Second * 5,
				Hits:      1,
			})
			if err != nil {
				b.Errorf("client.RateLimit() err: %s", err)
			}
		}
	})
}
func BenchmarkServer_NoOp(b *testing.B) {
	client, err := gubernator.NewClient(gubernator.RandomPeer(peers))
	if err != nil {
		b.Errorf("NewClient err: %s", err)
	}

	//dur := time.Nanosecond * 117728
	//total := time.Second / dur
	//fmt.Printf("Total: %d\n", total)

	b.Run("Ping", func(b *testing.B) {
		for n := 0; n < b.N; n++ {
			if err := client.Ping(context.Background()); err != nil {
				b.Errorf("client.Ping() err: %s", err)
			}
		}
	})
}

// TODO: Benchmark with fanout to simulate thundering heard of simultaneous requests from many clients