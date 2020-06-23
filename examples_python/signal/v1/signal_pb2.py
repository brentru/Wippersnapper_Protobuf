# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signal/v1/signal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='signal/v1/signal.proto',
  package='signal.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16signal/v1/signal.proto\x12\tsignal.v1\"\xf6\x04\n\x06Signal\x12*\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x19.signal.v1.Signal.Command\x1a\x86\x02\n\x07\x43ommand\x12\'\n\x04mode\x18\x01 \x01(\x0e\x32\x19.signal.v1.Signal.CmdMode\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.signal.v1.Signal.CmdType\x12\x1b\n\x03pin\x18\x03 \x01(\x0b\x32\x0e.signal.v1.Pin\x12#\n\x07version\x18\x04 \x01(\x0b\x32\x12.signal.v1.Version\x12\x1b\n\x03pwm\x18\x05 \x01(\x0b\x32\x0e.signal.v1.PWM\x12%\n\x08location\x18\x06 \x01(\x0b\x32\x13.signal.v1.Location\x12#\n\x07\x62\x61ttery\x18\x07 \x01(\x0b\x32\x12.signal.v1.Battery\"G\n\x07\x43mdMode\x12\x18\n\x14\x43MD_MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43MD_MODE_GET\x10\x01\x12\x10\n\x0c\x43MD_MODE_SET\x10\x02\"\xed\x01\n\x07\x43mdType\x12\x18\n\x14\x43MD_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43MD_TYPE_VERSION\x10\x01\x12\x15\n\x11\x43MD_TYPE_LOCATION\x10\x02\x12\x14\n\x10\x43MD_TYPE_BATTERY\x10\x03\x12\x1d\n\x19\x43MD_TYPE_LIST_PINS_ANALOG\x10\x04\x12\x1e\n\x1a\x43MD_TYPE_LIST_PINS_DIGITAL\x10\x05\x12\x16\n\x12\x43MD_TYPE_PIN_VALUE\x10\x06\x12\x15\n\x11\x43MD_TYPE_PIN_MODE\x10\x07\x12\x17\n\x13\x43MD_TYPE_PWM_OUTPUT\x10\x08\"E\n\x07Version\x12\r\n\x05major\x18\x01 \x01(\x04\x12\r\n\x05minor\x18\x02 \x01(\x04\x12\r\n\x05micro\x18\x03 \x01(\x04\x12\r\n\x05label\x18\x04 \x01(\t\"A\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x02\"\x18\n\x07\x42\x61ttery\x12\r\n\x05level\x18\x01 \x01(\x02\"\xf5\x02\n\x03Pin\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x04mode\x18\x02 \x01(\x0e\x32\x13.signal.v1.Pin.Mode\x12+\n\tdirection\x18\x03 \x01(\x0e\x32\x18.signal.v1.Pin.Direction\x12!\n\x04pull\x18\x04 \x01(\x0e\x32\x13.signal.v1.Pin.Pull\x12\r\n\x05value\x18\x05 \x01(\t\"Q\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_ANALOG\x10\x01\x12\x10\n\x0cMODE_DIGITAL\x10\x02\x12\x10\n\x0cMODE_PULL_UP\x10\x03\"Q\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x44IRECTION_INPUT\x10\x01\x12\x14\n\x10\x44IRECTION_OUTPUT\x10\x02\"8\n\x04Pull\x12\x14\n\x10PULL_UNSPECIFIED\x10\x00\x12\x0b\n\x07PULL_UP\x10\x01\x12\r\n\tPULL_DOWN\x10\x02\">\n\x03PWM\x12\x10\n\x08pin_name\x18\x01 \x01(\t\x12\x12\n\nduty_cycle\x18\x02 \x01(\x05\x12\x11\n\tfrequency\x18\x03 \x01(\x05\x62\x06proto3'
)



_SIGNAL_CMDMODE = _descriptor.EnumDescriptor(
  name='CmdMode',
  full_name='signal.v1.Signal.CmdMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_GET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_SET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=357,
  serialized_end=428,
)
_sym_db.RegisterEnumDescriptor(_SIGNAL_CMDMODE)

_SIGNAL_CMDTYPE = _descriptor.EnumDescriptor(
  name='CmdType',
  full_name='signal.v1.Signal.CmdType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_VERSION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_LOCATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_BATTERY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_LIST_PINS_ANALOG', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_LIST_PINS_DIGITAL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PIN_VALUE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PIN_MODE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PWM_OUTPUT', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=431,
  serialized_end=668,
)
_sym_db.RegisterEnumDescriptor(_SIGNAL_CMDTYPE)

_PIN_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='signal.v1.Pin.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_ANALOG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_DIGITAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_PULL_UP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=986,
  serialized_end=1067,
)
_sym_db.RegisterEnumDescriptor(_PIN_MODE)

_PIN_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='signal.v1.Pin.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_INPUT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_OUTPUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1069,
  serialized_end=1150,
)
_sym_db.RegisterEnumDescriptor(_PIN_DIRECTION)

_PIN_PULL = _descriptor.EnumDescriptor(
  name='Pull',
  full_name='signal.v1.Pin.Pull',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PULL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULL_UP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULL_DOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1152,
  serialized_end=1208,
)
_sym_db.RegisterEnumDescriptor(_PIN_PULL)


_SIGNAL_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='signal.v1.Signal.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='signal.v1.Signal.Command.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='signal.v1.Signal.Command.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pin', full_name='signal.v1.Signal.Command.pin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='signal.v1.Signal.Command.version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pwm', full_name='signal.v1.Signal.Command.pwm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='signal.v1.Signal.Command.location', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='signal.v1.Signal.Command.battery', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=93,
  serialized_end=355,
)

_SIGNAL = _descriptor.Descriptor(
  name='Signal',
  full_name='signal.v1.Signal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='signal.v1.Signal.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNAL_COMMAND, ],
  enum_types=[
    _SIGNAL_CMDMODE,
    _SIGNAL_CMDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=668,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='signal.v1.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='signal.v1.Version.major', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor', full_name='signal.v1.Version.minor', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='micro', full_name='signal.v1.Version.micro', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='signal.v1.Version.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=670,
  serialized_end=739,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='signal.v1.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='signal.v1.Location.latitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='signal.v1.Location.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='signal.v1.Location.altitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=741,
  serialized_end=806,
)


_BATTERY = _descriptor.Descriptor(
  name='Battery',
  full_name='signal.v1.Battery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='signal.v1.Battery.level', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=808,
  serialized_end=832,
)


_PIN = _descriptor.Descriptor(
  name='Pin',
  full_name='signal.v1.Pin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='signal.v1.Pin.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='signal.v1.Pin.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='signal.v1.Pin.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pull', full_name='signal.v1.Pin.pull', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='signal.v1.Pin.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PIN_MODE,
    _PIN_DIRECTION,
    _PIN_PULL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=1208,
)


_PWM = _descriptor.Descriptor(
  name='PWM',
  full_name='signal.v1.PWM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pin_name', full_name='signal.v1.PWM.pin_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='signal.v1.PWM.duty_cycle', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='signal.v1.PWM.frequency', index=2,
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
  serialized_start=1210,
  serialized_end=1272,
)

_SIGNAL_COMMAND.fields_by_name['mode'].enum_type = _SIGNAL_CMDMODE
_SIGNAL_COMMAND.fields_by_name['type'].enum_type = _SIGNAL_CMDTYPE
_SIGNAL_COMMAND.fields_by_name['pin'].message_type = _PIN
_SIGNAL_COMMAND.fields_by_name['version'].message_type = _VERSION
_SIGNAL_COMMAND.fields_by_name['pwm'].message_type = _PWM
_SIGNAL_COMMAND.fields_by_name['location'].message_type = _LOCATION
_SIGNAL_COMMAND.fields_by_name['battery'].message_type = _BATTERY
_SIGNAL_COMMAND.containing_type = _SIGNAL
_SIGNAL.fields_by_name['command'].message_type = _SIGNAL_COMMAND
_SIGNAL_CMDMODE.containing_type = _SIGNAL
_SIGNAL_CMDTYPE.containing_type = _SIGNAL
_PIN.fields_by_name['mode'].enum_type = _PIN_MODE
_PIN.fields_by_name['direction'].enum_type = _PIN_DIRECTION
_PIN.fields_by_name['pull'].enum_type = _PIN_PULL
_PIN_MODE.containing_type = _PIN
_PIN_DIRECTION.containing_type = _PIN
_PIN_PULL.containing_type = _PIN
DESCRIPTOR.message_types_by_name['Signal'] = _SIGNAL
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Battery'] = _BATTERY
DESCRIPTOR.message_types_by_name['Pin'] = _PIN
DESCRIPTOR.message_types_by_name['PWM'] = _PWM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Signal = _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {

  'Command' : _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
    'DESCRIPTOR' : _SIGNAL_COMMAND,
    '__module__' : 'signal.v1.signal_pb2'
    # @@protoc_insertion_point(class_scope:signal.v1.Signal.Command)
    })
  ,
  'DESCRIPTOR' : _SIGNAL,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Signal)
  })
_sym_db.RegisterMessage(Signal)
_sym_db.RegisterMessage(Signal.Command)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Version)
  })
_sym_db.RegisterMessage(Version)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Location)
  })
_sym_db.RegisterMessage(Location)

Battery = _reflection.GeneratedProtocolMessageType('Battery', (_message.Message,), {
  'DESCRIPTOR' : _BATTERY,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Battery)
  })
_sym_db.RegisterMessage(Battery)

Pin = _reflection.GeneratedProtocolMessageType('Pin', (_message.Message,), {
  'DESCRIPTOR' : _PIN,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Pin)
  })
_sym_db.RegisterMessage(Pin)

PWM = _reflection.GeneratedProtocolMessageType('PWM', (_message.Message,), {
  'DESCRIPTOR' : _PWM,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.PWM)
  })
_sym_db.RegisterMessage(PWM)


# @@protoc_insertion_point(module_scope)
