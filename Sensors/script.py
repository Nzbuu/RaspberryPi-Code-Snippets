from Thermistor import Thermistor
from DataLog import DataLog
#from DummySensor import DummySensor

try:
    # Create global variable for pinslse
    pin_in = 17
    pin_out  = 13
    Capacitance = 10e-6 # Capacitance [F]

    sensor = Thermistor(pin_in, pin_out, Capacitance)
    #sensor = DummySensor()
    timeStepRead = 10
    timeStepWrite = 30
    d = DataLog(sensor, timeStepRead, timeStepWrite)
    d.run()

finally:
    del sensor
