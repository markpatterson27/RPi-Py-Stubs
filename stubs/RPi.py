# stubs for RPi module
from random import randint


class _GPIO(object):

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
    def cleanup(self, channel=None):
        pass

    def setup(self, channel, direction, initial=0, pull_up_down=PUD_OFF):
        pass

    def output(self, channel, value):
        pass

    def input(self, channel):
        return randint(0, 1)

    def setmode(self, mode):
        pass

    def getmode(self):
        return self.BCM

    def add_event_callback(self, gpio, callback):
        pass

    def add_event_detect(self, gpio, edge, callback=None, bouncetime=None):
        pass

    def remove_event_detect(self, gpio):
        pass

    def event_detected(self, channel):
        return False

    def wait_for_edge(self, channel, edge, bouncetime=None, timeout=None):
        pass

    def gpio_function(self, channel):
        return GPIO.OUT

    def setwarnings(self, state):
        pass


GPIO = _GPIO()   
