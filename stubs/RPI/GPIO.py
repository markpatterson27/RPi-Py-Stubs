
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


# Define PWM
class PWM(object):

    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.dc = 0

    def start(self, dutycycle):
        pass

    def ChangeDutyCycle(self, dutycycle):
        self.dc = dutycycle

    def ChangeFrequency(self, frequency):
        self.frequency = frequency

    def stop(self):
        pass

# Define functions
def cleanup(channel=None):
    pass

def setup(channel, direction, initial=0, pull_up_down=PUD_OFF):
    pass

def output(channel, value):
    pass

def input(channel):
    return randint(0, 1)

def setmode(mode):
    pass

def getmode():
    return BCM

def add_event_callback(gpio, callback):
    pass

def add_event_detect(gpio, edge, callback=None, bouncetime=None):
    pass

def remove_event_detect(gpio):
    pass

def event_detected(channel):
    return False

def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
    pass

def gpio_function(channel):
    return OUT

def setwarnings(state):
    pass
