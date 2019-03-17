# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratelimit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ratelimit.proto',
  package='pb.gubernator',
  syntax='proto3',
  serialized_options=_b('Z\002pb\200\001\001'),
  serialized_pb=_b('\n\x0fratelimit.proto\x12\rpb.gubernator\x1a\x1cgoogle/api/annotations.proto\"L\n\x14RateLimitRequestList\x12\x34\n\x0brate_limits\x18\x01 \x03(\x0b\x32\x1f.pb.gubernator.RateLimitRequest\"N\n\x15RateLimitResponseList\x12\x35\n\x0brate_limits\x18\x01 \x03(\x0b\x32 .pb.gubernator.RateLimitResponse\"\xc0\x01\n\x10RateLimitRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\nunique_key\x18\x02 \x01(\t\x12\x0c\n\x04hits\x18\x03 \x01(\x03\x12\r\n\x05limit\x18\x04 \x01(\x03\x12\x10\n\x08\x64uration\x18\x05 \x01(\x03\x12+\n\talgorithm\x18\x06 \x01(\x0e\x32\x18.pb.gubernator.Algorithm\x12)\n\x08\x62\x65havior\x18\x07 \x01(\x0e\x32\x17.pb.gubernator.Behavior\"\x80\x02\n\x11RateLimitResponse\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.pb.gubernator.Status\x12\x15\n\rcurrent_limit\x18\x02 \x01(\x03\x12\x17\n\x0flimit_remaining\x18\x03 \x01(\x03\x12\x12\n\nreset_time\x18\x04 \x01(\x03\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12@\n\x08metadata\x18\x06 \x03(\x0b\x32..pb.gubernator.RateLimitResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x14\n\x12HealthCheckRequest\"J\n\x13HealthCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\npeer_count\x18\x03 \x01(\x05*/\n\tAlgorithm\x12\x10\n\x0cTOKEN_BUCKET\x10\x00\x12\x10\n\x0cLEAKY_BUCKET\x10\x01*5\n\x08\x42\x65havior\x12\x0c\n\x08\x42\x41TCHING\x10\x00\x12\x0f\n\x0bNO_BATCHING\x10\x01\x12\n\n\x06GLOBAL\x10\x02*)\n\x06Status\x12\x0f\n\x0bUNDER_LIMIT\x10\x00\x12\x0e\n\nOVER_LIMIT\x10\x01\x32\xfb\x01\n\x10RateLimitService\x12x\n\rGetRateLimits\x12#.pb.gubernator.RateLimitRequestList\x1a$.pb.gubernator.RateLimitResponseList\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/GetRateLimits:\x01*\x12m\n\x0bHealthCheck\x12!.pb.gubernator.HealthCheckRequest\x1a\".pb.gubernator.HealthCheckResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/HealthCheckB\x07Z\x02pb\x80\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='pb.gubernator.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOKEN_BUCKET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAKY_BUCKET', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=774,
  serialized_end=821,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHM)

Algorithm = enum_type_wrapper.EnumTypeWrapper(_ALGORITHM)
_BEHAVIOR = _descriptor.EnumDescriptor(
  name='Behavior',
  full_name='pb.gubernator.Behavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATCHING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_BATCHING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=823,
  serialized_end=876,
)
_sym_db.RegisterEnumDescriptor(_BEHAVIOR)

Behavior = enum_type_wrapper.EnumTypeWrapper(_BEHAVIOR)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pb.gubernator.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDER_LIMIT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVER_LIMIT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=878,
  serialized_end=919,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
TOKEN_BUCKET = 0
LEAKY_BUCKET = 1
BATCHING = 0
NO_BATCHING = 1
GLOBAL = 2
UNDER_LIMIT = 0
OVER_LIMIT = 1



_RATELIMITREQUESTLIST = _descriptor.Descriptor(
  name='RateLimitRequestList',
  full_name='pb.gubernator.RateLimitRequestList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate_limits', full_name='pb.gubernator.RateLimitRequestList.rate_limits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=140,
)


_RATELIMITRESPONSELIST = _descriptor.Descriptor(
  name='RateLimitResponseList',
  full_name='pb.gubernator.RateLimitResponseList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate_limits', full_name='pb.gubernator.RateLimitResponseList.rate_limits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=220,
)


_RATELIMITREQUEST = _descriptor.Descriptor(
  name='RateLimitRequest',
  full_name='pb.gubernator.RateLimitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pb.gubernator.RateLimitRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_key', full_name='pb.gubernator.RateLimitRequest.unique_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hits', full_name='pb.gubernator.RateLimitRequest.hits', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='pb.gubernator.RateLimitRequest.limit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='pb.gubernator.RateLimitRequest.duration', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='pb.gubernator.RateLimitRequest.algorithm', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behavior', full_name='pb.gubernator.RateLimitRequest.behavior', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=415,
)


_RATELIMITRESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='pb.gubernator.RateLimitResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pb.gubernator.RateLimitResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb.gubernator.RateLimitResponse.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=674,
)

_RATELIMITRESPONSE = _descriptor.Descriptor(
  name='RateLimitResponse',
  full_name='pb.gubernator.RateLimitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pb.gubernator.RateLimitResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_limit', full_name='pb.gubernator.RateLimitResponse.current_limit', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_remaining', full_name='pb.gubernator.RateLimitResponse.limit_remaining', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_time', full_name='pb.gubernator.RateLimitResponse.reset_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pb.gubernator.RateLimitResponse.error', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pb.gubernator.RateLimitResponse.metadata', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RATELIMITRESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=674,
)


_HEALTHCHECKREQUEST = _descriptor.Descriptor(
  name='HealthCheckRequest',
  full_name='pb.gubernator.HealthCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=676,
  serialized_end=696,
)


_HEALTHCHECKRESPONSE = _descriptor.Descriptor(
  name='HealthCheckResponse',
  full_name='pb.gubernator.HealthCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pb.gubernator.HealthCheckResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pb.gubernator.HealthCheckResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer_count', full_name='pb.gubernator.HealthCheckResponse.peer_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=772,
)

_RATELIMITREQUESTLIST.fields_by_name['rate_limits'].message_type = _RATELIMITREQUEST
_RATELIMITRESPONSELIST.fields_by_name['rate_limits'].message_type = _RATELIMITRESPONSE
_RATELIMITREQUEST.fields_by_name['algorithm'].enum_type = _ALGORITHM
_RATELIMITREQUEST.fields_by_name['behavior'].enum_type = _BEHAVIOR
_RATELIMITRESPONSE_METADATAENTRY.containing_type = _RATELIMITRESPONSE
_RATELIMITRESPONSE.fields_by_name['status'].enum_type = _STATUS
_RATELIMITRESPONSE.fields_by_name['metadata'].message_type = _RATELIMITRESPONSE_METADATAENTRY
DESCRIPTOR.message_types_by_name['RateLimitRequestList'] = _RATELIMITREQUESTLIST
DESCRIPTOR.message_types_by_name['RateLimitResponseList'] = _RATELIMITRESPONSELIST
DESCRIPTOR.message_types_by_name['RateLimitRequest'] = _RATELIMITREQUEST
DESCRIPTOR.message_types_by_name['RateLimitResponse'] = _RATELIMITRESPONSE
DESCRIPTOR.message_types_by_name['HealthCheckRequest'] = _HEALTHCHECKREQUEST
DESCRIPTOR.message_types_by_name['HealthCheckResponse'] = _HEALTHCHECKRESPONSE
DESCRIPTOR.enum_types_by_name['Algorithm'] = _ALGORITHM
DESCRIPTOR.enum_types_by_name['Behavior'] = _BEHAVIOR
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RateLimitRequestList = _reflection.GeneratedProtocolMessageType('RateLimitRequestList', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITREQUESTLIST,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimitRequestList)
  ))
_sym_db.RegisterMessage(RateLimitRequestList)

RateLimitResponseList = _reflection.GeneratedProtocolMessageType('RateLimitResponseList', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITRESPONSELIST,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimitResponseList)
  ))
_sym_db.RegisterMessage(RateLimitResponseList)

RateLimitRequest = _reflection.GeneratedProtocolMessageType('RateLimitRequest', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITREQUEST,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimitRequest)
  ))
_sym_db.RegisterMessage(RateLimitRequest)

RateLimitResponse = _reflection.GeneratedProtocolMessageType('RateLimitResponse', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _RATELIMITRESPONSE_METADATAENTRY,
    __module__ = 'ratelimit_pb2'
    # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimitResponse.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _RATELIMITRESPONSE,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimitResponse)
  ))
_sym_db.RegisterMessage(RateLimitResponse)
_sym_db.RegisterMessage(RateLimitResponse.MetadataEntry)

HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKREQUEST,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.HealthCheckRequest)
  ))
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType('HealthCheckResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKRESPONSE,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.HealthCheckResponse)
  ))
_sym_db.RegisterMessage(HealthCheckResponse)


DESCRIPTOR._options = None
_RATELIMITRESPONSE_METADATAENTRY._options = None

_RATELIMITSERVICE = _descriptor.ServiceDescriptor(
  name='RateLimitService',
  full_name='pb.gubernator.RateLimitService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=922,
  serialized_end=1173,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRateLimits',
    full_name='pb.gubernator.RateLimitService.GetRateLimits',
    index=0,
    containing_service=None,
    input_type=_RATELIMITREQUESTLIST,
    output_type=_RATELIMITRESPONSELIST,
    serialized_options=_b('\202\323\344\223\002\026\"\021/v1/GetRateLimits:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='HealthCheck',
    full_name='pb.gubernator.RateLimitService.HealthCheck',
    index=1,
    containing_service=None,
    input_type=_HEALTHCHECKREQUEST,
    output_type=_HEALTHCHECKRESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\022\017/v1/HealthCheck'),
  ),
])
_sym_db.RegisterServiceDescriptor(_RATELIMITSERVICE)

DESCRIPTOR.services_by_name['RateLimitService'] = _RATELIMITSERVICE

# @@protoc_insertion_point(module_scope)
