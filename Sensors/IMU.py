import smbus
from sensor_sheet import registers
import numpy as np
import time
from measurement import Measurement


class IMU:
    """ Measures rotation and translation """
    # Datasheet for the IMU can be found at
    # http://ozzmaker.com/wp-content/uploads/2014/12/LSM9DS0.pdf
    sensorType = "IMU"
    sensorID = "BerryIMU"

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address_book = registers
        self.__enableSensor()

    def __del__(self):
        pass

    def printResults(self):
        pass

    def readBlock(self, address, command):

        register = self.address_book[command]
        block_length = 6  # length of block to read in bytes
        block = np.uint8( self.bus.read_i2c_block_data(address, 0x80 | register, block_length))

        block = block.reshape(3,2)  # assumes that x,y and z data where read in

        block = [np.int16(row[0] | row[1] <<8) for row in block] # combine two's complement values into integer
        return block

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

    def getMagMeasurement(self):
        address = self.address_book['MAG_ADDRESS']
        raw_data = self.readBlock(address, 'OUT_X_L_M')
        time_meas = time.time()
        mag_LSB = 0.48 * 1e-3  # G/LSB  TODO: make this dependent on the initialisation command
        factor_tesla_per_gauss = 1e-4  # http://en.wikipedia.org/wiki/Gauss_%28unit%29
        mag_flux_density = [row * mag_LSB * factor_tesla_per_gauss for row in raw_data]

        # Create new measurement object
        newMeasurement = Measurement()
        newMeasurement.timeStamp = time_meas
        newMeasurement.value = mag_flux_density
        newMeasurement.units = 'T'
        return newMeasurement

    def getAccMeasurement(self):
        address = self.address_book['ACC_ADDRESS']
        raw_data = self.readBlock(address, 'OUT_X_L_A')
        time_meas = time.time()
        acc_LSB = 0.732 * 1e-3  # g/LSB  TODO: make this dependent on the initialisation command
        factor_ms2_per_gn = 9.80665  # From http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf#page=51
        acc = [row * acc_LSB * factor_ms2_per_gn for row in raw_data]

        # Create new measurement object
        newMeasurement = Measurement()
        newMeasurement.timeStamp = time_meas
        newMeasurement.value = acc
        newMeasurement.units = 'm/s^2'
        return newMeasurement

    def getGyrMeasurement(self):
        address = self.address_book['GYR_ADDRESS']
        time_before = time.time()
        raw_data = self.readBlock(address, 'OUT_X_L_G')
        time_meas = time.time()
        deltaT = time_meas-time_before
        print "max measurement delay [s]" + deltaT

        gyr_LSB = 0.07  # deg/s/LSB TODO: make this dependent on the initialisation command
        factor_rad_per_deg = 180 / np.pi
        rate = [row * gyr_LSB * factor_rad_per_deg for row in raw_data]

        # Create new measurement object
        newMeasurement = Measurement()
        newMeasurement.timeStamp = time_meas
        newMeasurement.value = rate
        newMeasurement.units = 'rad/s'
        return newMeasurement

    def __enableSensor(self):
        # Enable accelerometer.
        self.writeAccReg('CTRL_REG1_XM', 0b01100111)  # z,y,x axis enabled, continuous update,  100Hz data rate
        self.writeAccReg('CTRL_REG2_XM', 0b00100000)  # +/- 16G full scale.  This determines the LSB

        # Enable the magnetometer
        self.writeMagReg('CTRL_REG5_XM', 0b11110000)   # Temp enable, M data rate = 50Hz
        self.writeMagReg( 'CTRL_REG6_XM', 0b01100000)   # +/-12gauss. This determines the LSB
        self.writeMagReg( 'CTRL_REG7_XM', 0b00000000)   # Continuous-conversion mode

        # Enable Gyro
        self.writeGyrReg('CTRL_REG1_G', 0b00001111)  # Normal power mode, all axes enabled
        self.writeGyrReg('CTRL_REG4_G', 0b00110000)  # Continuous update, Data LSb @ lower address, 2000 dps full scale. This determines the LSB
