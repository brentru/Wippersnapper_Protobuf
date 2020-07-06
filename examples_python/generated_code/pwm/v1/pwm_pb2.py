# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pwm/v1/pwm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pwm/v1/pwm.proto',
  package='pwm.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10pwm/v1/pwm.proto\x12\x06pwm.v1\">\n\x03PWM\x12\x10\n\x08pin_name\x18\x01 \x01(\t\x12\x12\n\nduty_cycle\x18\x02 \x01(\x05\x12\x11\n\tfrequency\x18\x03 \x01(\x05\x62\x06proto3'
)




_PWM = _descriptor.Descriptor(
  name='PWM',
  full_name='pwm.v1.PWM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pin_name', full_name='pwm.v1.PWM.pin_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='pwm.v1.PWM.duty_cycle', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='pwm.v1.PWM.frequency', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['PWM'] = _PWM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PWM = _reflection.GeneratedProtocolMessageType('PWM', (_message.Message,), {
  'DESCRIPTOR' : _PWM,
  '__module__' : 'pwm.v1.pwm_pb2'
  # @@protoc_insertion_point(class_scope:pwm.v1.PWM)
  })
_sym_db.RegisterMessage(PWM)


# @@protoc_insertion_point(module_scope)