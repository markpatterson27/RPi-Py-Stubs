# stubs for smbus module
from random import randint

class SMBus(object):

    def __init__(self, bus=None, force=False):
        self.bus = bus
        self.force = force

    def write_byte_data(self, i2c_addr, register, value):
        pass

    def write_byte(self, i2c_addr, value):
        pass

    def read_byte_data(self, i2c_addr, register):
        return randint(0, 2**8-1)

    def read_byte(self, i2c_addr):
        return randint(0, 2**8-1)

    def read_word_data(self, i2c_addr, register):
        return randint(0, 2**16-1)

    def write_word_data(self, i2c_addr, register, value):
        pass

    def read_i2c_block_data(self, i2c_addr, register, len=32):
        return [randint(0, 2**8-1)]*len

    def write_i2c_block_data(self, i2c_addr, register, data):
        pass

    def open(self, bus):
        pass

    def close(self):
        pass


# SMBus = _SMBus()
