'''
Stub version of smbus module.

This module defines an object type that allows SMBus transactions on hosts
running the Linux kernel. The host kernel must have I2C support, I2C device
interface support, and a bus adapter driver. All of these can be either built-in
to the kernel, or loaded from modules.

Because the I2C device interface is opened R/W, users of this module usually
must have root permissions.
'''
from random import randint

class SMBus(object):
    '''
    SMBus([bus]) -> SMBus

    Return a new SMBus object that is (optionally) connected to the specified I2C device interface.
    '''

    def __init__(self, bus=None, force=False):
        self.bus = bus
        self.force = force

    def open(self, bus):
        '''
        open(bus)

        Connects the object to the specified SMBus.
        '''
        pass

    def close(self):
        '''Disconnects the object from the bus.'''
        pass

    def process_call(self, addr, cmd, val):
        '''Perform SMBus Process Call transaction.'''
        pass

    def block_process_call(self, addr, cmd, vals=None):
        '''
        block_process_call(addr, cmd, [vals]) -> results

        Perform SMBus Block Process Call transaction.
        '''
        return randint(0, 2**8-1)

    def read_block_data(self, addr, cmd):
        '''
        read_block_data(addr, cmd) -> results

        Perform SMBus Read Block Data transaction.
        '''
        return randint(0, 2**8-1)

    def read_byte(self, addr):
        '''
        read_byte(addr) -> result

        Perform SMBus Read Byte transaction.
        '''
        return randint(0, 2**8-1)

    def read_byte_data(self, addr, cmd):
        '''
        read_byte_data(addr, cmd) -> result

        Perform SMBus Read Byte Data transaction.
        '''
        return randint(0, 2**8-1)

    def read_i2c_block_data(self, addr, cmd, len=32):
        '''
        read_i2c_block_data(addr, cmd, len=32) -> results

        Perform I2C Block Read transaction.
        '''
        return [randint(0, 2**8-1)]*len

    def read_word_data(self, addr, cmd):
        '''
        read_word_data(addr, cmd) -> result

        Perform SMBus Read Word Data transaction.
        '''
        return randint(0, 2**16-1)

    def write_block_data(self, addr, cmd, vals=None):
        '''
        write_block_data(addr, cmd, [vals])

        Perform SMBus Write Block Data transaction.
        '''
        pass

    def write_byte(self, addr, val):
        '''Perform SMBus Write Byte transaction.'''
        pass

    def write_byte_data(self, addr, cmd, val):
        '''Perform SMBus Write Byte Data transaction.'''
        pass

    def write_i2c_block_data(self, addr, cmd, vals=None):
        '''
        write_i2c_block_data(addr, cmd, [vals])

        Perform I2C Block Write transaction.
        '''
        pass

    def write_quick(self, addr):
        '''Perform SMBus Quick transaction.'''
        pass

    def write_word_data(self, addr, cmd, val):
        '''Perform SMBus Write Word Data transaction.'''
        pass


# SMBus = _SMBus()
