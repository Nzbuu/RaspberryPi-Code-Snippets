#from DS18B20 import DS18B20
from DataLog import DataLog
from DummySensor import DummySensor

try:

    #sensor = DS18B20()
    sensor = DummySensor()
    timeStepRead = 1
    timeStepWrite = 3
    d = DataLog(sensor, timeStepRead, timeStepWrite)
    d.run()

finally:
    del sensor