# SPDX-FileCopyrightText: 2020 Brent Rubell for Adafruit Industries
# SPDX-License-Identifier: MIT
import sys
sys.path.insert(1, 'signal/v1')

import signal_pb2

# Create new signal message
signal = signal_pb2.Signal()

"""
Configure digital pin D3 as a digital input
"""
cmd = signal.command
# command message
cmd.mode = signal.CMD_MODE_SET
cmd.type = signal.CMD_TYPE_PIN_MODE
# pin message
cmd.pin.name = "D3"
cmd.pin.mode = signal.command.pin.MODE_DIGITAL
cmd.pin.direction = signal.command.pin.DIRECTION_INPUT

print(signal)
signal.Clear()


"""
GET value of pin D3 from Adafruit IO
"""
cmd = signal.command
# command message
cmd.mode = signal.CMD_MODE_GET
cmd.type = signal.CMD_TYPE_PIN_VALUE
# pin message
cmd.pin.name = "D3"

print(signal)
signal.Clear()

"""
SET value of pin D3
"""
cmd = signal.command
# command message
cmd.mode = signal.CMD_MODE_GET
cmd.type = signal.CMD_TYPE_PIN_VALUE
# pin message
cmd.pin.name = "D3"
cmd.pin.value = "1"

print(signal)
signal.Clear()