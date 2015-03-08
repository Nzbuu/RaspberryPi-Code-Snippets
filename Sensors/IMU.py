import smbus
from registers import registers
import time
from measurement import Measurement


class IMU:
    """ Measures rotation and translation """
    # Datasheet for the IMU can be found at
    # http://ozzmaker.com/wp-content/uploads/2014/12/LSM9DS0.pdf
    sensorType = "IMU"
    sensorID = "BerryIMU"
    sensorUnits = "var"

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address_book = registers
        self.enableSensor()

    def __del__(self):
        pass

    def getMeasurement(self):
        pass

    def printResults(self):
        pass

    def readBlock(self, address, register, length):
        self.bus.read_block_data(address, register, length)

    def writeMagReg(self, command, value):
        address = self.address_book['MAG_ADDRESS']
        register = self.address_book[command]
        self.bus.write_byte_data(address, register, value)

    def writeAccReg(self, command, value):
        address = self.address_book['ACC_ADDRESS']
        register = self.address_book[command]
        self.bus.write_byte_data(address, register, value)

    def writeGyrReg(self, command, value):
        address = self.address_book['GYR_ADDRESS']
        register = self.address_book[command]
        self.bus.write_byte_data(address, register, value)

    def readMagReg(self, command):
        address = self.address_book['MAG_ADDRESS']
        register = self.address_book[command]
        value = self.bus.read_byte_data(address, register)
        return value

    def readAccReg(self, command):
        address = self.address_book['ACC_ADDRESS']
        register = self.address_book[command]
        value = self.bus.readBlock(address, register)
        return value

    def readGyrReg(self, command):
        address = self.address_book['GYR_ADDRESS']
        register = self.address_book[command]
        value = self.bus.read_byte_data(address, register)
        return value

    def enableSensor(self):
        # Enable accelerometer.
        self.writeAccReg('CTRL_REG1_XM', 0b01100111)  # z,y,x axis enabled, continuous update,  100Hz data rate
        self.writeAccReg('CTRL_REG2_XM', 0b00100000)  # +/- 16G full scale

        # Enable the magnetometer
        self.writeMagReg('CTRL_REG5_XM', 0b11110000)   # Temp enable, M data rate = 50Hz
        self.writeMagReg( 'CTRL_REG6_XM', 0b01100000)   # +/-12gauss
        self.writeMagReg( 'CTRL_REG7_XM', 0b00000000)   # Continuous-conversion mode

        # Enable Gyro
        self.writeGyrReg('CTRL_REG1_G', 0b00001111)  # Normal power mode, all axes enabled
        self.writeGyrReg('CTRL_REG4_G', 0b00110000)  # Continuous update, 2000 dps full scale


    def __readSensor(self):
        pass

    def __formatSensorData(self, stringInput):
        pass
