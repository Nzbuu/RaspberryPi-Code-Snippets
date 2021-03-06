import RPi.GPIO as GPIO
import time
import math

class Thermistor:
    """ Measures Temperature using a Thermistor """
    # Class variable: Sensor type
    sensorType = "Thermometer"
    sensorID = "Thermistor"
    sensorUnits = "degC"

    def __init__(self, pin_in, pin_out, C):
        # Set pins
        self.pin_in = pin_in
        self.pin_out = pin_out
        self.Capacitance = C # Capacitance [F]

        self.tau = 0
        self.temperature = 0

        # Set up GPIO    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_out, GPIO.OUT)
        # Initialise output voltage to zero.
        GPIO.output(pin_out, GPIO.LOW)
    
        # When the output pin is low in the circuit, the input is pulled down to low
        GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
    
    def __del__(self):
        GPIO.cleanup()
 
    def __calculateTimeConstant(self):  
        timeCharge = self.__countToHigh()
        self.tau = timeCharge/math.log(2)

    def __calculateTemperature(self):
        Resistance = self.tau / self.Capacitance # Thermistor resistance

        # Use Steinhart and Hart Equation to calculate temperature
        A = 3.354016E-03
        B = 2.569850E-04
        C = 2.620131E-06
        D = 6.383091E-08
        Resistance_ref = 10000
    
        lr = math.log(Resistance/Resistance_ref)
        inverseOfT = A + B * lr + C * math.pow(lr,2) + D * math.pow(lr,3)

        T = 1/inverseOfT
        self.temperature = T - 273.15  # convert from Kelvin to degCelsius

    def getMeasurement(self):
        self.__calculateTimeConstant()
        self.__calculateTemperature()
        class Measurement:
            timeStamp = 0
            data = 0
            units = 0

        newMeasurement = Measurement()
        newMeasurement.timeStamp = time.time()
        newMeasurement.data = self.temperature
        newMeasurement.units = self.sensorUnits

        return newMeasurement


    def printResults(self):
        print "Time constant: " + str(round(tau*1000,1)) + "ms."
        print "Temperature = " + str(round(self.temperature,1)) + " " + self.sensorUnits

    def __countToHigh(self):

        count = 0
        # Set the output state to high (this charges the capacitor)
        startTime = time.time()

        GPIO.output(self.pin_out, GPIO.HIGH)
    
        while GPIO.input(self.pin_in) == GPIO.LOW:
            count +=1

        diffTime=time.time() - startTime
    
        # Reset output pin to low
        GPIO.output(self.pin_out, GPIO.LOW)
        time.sleep(0.1)
        return diffTime       


