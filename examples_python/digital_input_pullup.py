# SPDX-FileCopyrightText: 2020 Brent Rubell for Adafruit Industries
# SPDX-License-Identifier: MIT

import signal_pb2

def serialize_protobuf(buf):
    """Serializes protobuf
    to a string. Displays the protobuf and
    the protobuf information.

    """
    buf = buf.SerializeToString()
    print('Serialized Protobuf: ', buf)
    print('length: %i bytes'%len(buf))

# Create new signal message
signal = signal_pb2.Signal()

"""
PUBLISH from Adafruit IO to Device

Set up digital input switch with a pull up.
"""
command = signal.cmd
# command message
command.type = signal.CMD_TYPE_SET
command.name = signal.CMD_NAME_PIN_MODE
# pin message
command.pin_info.pin = "D5"
command.pin_info.mode = signal.pin_info.MODE_DIGITAL
command.pin_info.direction = signal.pin_info.DIRECTION_INPUT
command.pin_info.pull = signal.pin_info.PULL_UP

print(signal)
serialize_protobuf(signal)
signal.Clear()

"""
PUBLISH from Adafruit IO to Device

Obtain logic level of the pin.
"""
command = signal.cmd
# command message
command.type = signal.CMD_TYPE_GET
command.name = signal.CMD_NAME_PIN_VALUE
# pin message
command.pin_info.pin = "D5"

print(signal)
serialize_protobuf(signal)
signal.Clear()


"""
PUBLISH from Device to Adafruit IO

Send digital logic level of the pin from the
device to Adafruit IO.
"""
command = signal.cmd
# command message
command.type = signal.CMD_TYPE_SET
command.name = signal.CMD_NAME_PIN_VALUE
# pin message
command.pin_info.pin = "D5"
command.pin_info.value = "1"
print(signal)
serialize_protobuf(signal)
signal.Clear()