from IMU import IMU
from DataLog import DataLog

try:

    sensor = IMU()
    timeStepRead = 1
    timeStepWrite = 10
    d = DataLog(sensor, timeStepRead, timeStepWrite)
    d.run()

finally:
    del sensor