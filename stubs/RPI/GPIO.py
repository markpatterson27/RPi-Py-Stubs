"""
Stub version of a Python module to control the GPIO on a Raspberry Pi
"""
# Stub of RPi.GPIO. Original from https://sourceforge.net/projects/raspberry-gpio-python/
# 
# Copyright (c) 2012-2021 Ben Croston
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import randint

# Define constants
UNKNOWN = -1

# values
LOW = 0
HIGH = 1

# modes
BOARD = 10
BCM = 11

# functions
OUT = 0
IN = 1
SERIAL = 40
SPI = 41
I2C = 42
HARD_PWM = 43

# pull
PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

# edges
RISING = 31
FALLING = 32
BOTH = 33

# version info
RPI_REVISION = 3
VERSION = '0.1.0'
RPI_INFO = {
    'P1_REVISION': 3,
    'REVISION': "a00000",
    'TYPE': "stub",
    'MANUFACTURER': "stub",
    'PROCESSOR': "stub",
    'RAM': "4G",
    'INFO': "stub"
}

# globals
_mode = None


# Define PWM
class PWM(object):
    '''Pulse Width Modulation class'''

    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.dc = 0

    def start(self, dutycycle):
        '''Start software PWM dutycycle - the duty cycle (0.0 to 100.0)'''
        pass

    def ChangeDutyCycle(self, dutycycle):
        '''Change the duty cycle dutycycle - between 0.0 and 100.0'''
        self.dc = dutycycle

    def ChangeFrequency(self, frequency):
        '''Change the frequency frequency - frequency in Hz (freq > 1.0)'''
        self.frequency = frequency

    def stop(self):
        '''Stop software PWM'''
        pass

# Define functions
def cleanup(channel=None):
    '''
    Clean up by resetting all GPIO channels that have been used by this program
    to INPUT with no pullup/pulldown and no event detection
    [channel] - individual channel or list/tuple of channels to clean up.
    Default - clean every channel that has been used.
    '''
    pass

def setup(channel, direction, initial=0, pull_up_down=PUD_OFF):
    '''
    Set up a GPIO channel or list of channels with a direction and (optional)
    pull/up down control
    channel - either board pin number or BCM number depending on which mode is set.
    direction - IN or OUT
    [pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN
    [initial] - Initial value for an output channel
    '''
    pass

def output(channel, value):
    '''
    Output to a GPIO channel or list of channels
    channel - either board pin number or BCM number depending on which mode is set.
    value - 0/1 or False/True or LOW/HIGH
    '''
    pass

def input(channel):
    '''
    Input from a GPIO channel. Returns HIGH=1=True or LOW=0=False
    channel - either board pin number or BCM number depending on which mode is set.
    '''
    return randint(0, 1)

def setmode(mode):
    '''
    Set up numbering mode to use for channels.
    BOARD - Use Raspberry Pi board numbers
    BCM - Use Broadcom GPIO 00..nn numbers
    '''
    _mode = mode

def getmode():
    '''
    Get numbering mode used for channel numbers. Returns BOARD, BCM or None
    '''
    return _mode

def add_event_callback(channel, callback):
    '''
    Add a callback for an event already defined using add_event_detect()
    channel - either board pin number or BCM number depending on which mode is set.
    callback - a callback function
    '''
    pass

def add_event_detect(channel, edge, callback=None, bouncetime=None):
    '''
    param optional

    Enable edge detection events for a particular GPIO channel.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [callback]   - A callback function for the event (optional)
    [bouncetime] - Switch bounce timeout in ms for callback
    '''
    pass

def remove_event_detect(channel):
    '''
    Remove edge detection for a particular GPIO channel
    channel - either board pin number or BCM number depending on which mode is set.
    '''
    pass

def event_detected(channel):
    '''
    Returns True if an edge has occurred on a given GPIO.  You need to enable
    edge detection using add_event_detect() first.
    channel - either board pin number or BCM number depending on which mode is set.
    '''
    return False

def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
    '''
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [bouncetime] - time allowed between calls to allow for switchbounce
    [timeout]    - timeout in ms
    '''
    pass

def gpio_function(channel):
    '''
    param IN

    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)
    channel - either board pin number or BCM number depending on which mode is set.
    '''
    return OUT

def setwarnings(state):
    '''
    Enable or disable warning messages
    '''
    pass
