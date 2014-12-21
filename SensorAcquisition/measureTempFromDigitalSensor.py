from DS18B20 import DS18B20
from DataLog import DataLog
#from DummySensor import DummySensor

try:

    sensor = DS18B20()
    #sensor = DummySensor()
    timeStepRead = 10
    timeStepWrite = 30
    d = DataLog(sensor, timeStepRead, timeStepWrite)
    d.run()

finally:
    del sensor