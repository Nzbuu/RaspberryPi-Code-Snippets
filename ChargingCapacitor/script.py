import RPi.GPIO as GPIO
import time
import math

def countToHigh(pin_in, pin_out):
    count = 0
    # Set the output state to high (this charges the capacitor)
    startTime=time.time()

    GPIO.output(pin_out, GPIO.HIGH)
    
    while (GPIO.input(pin_in) == GPIO.LOW):
        count +=1

    diffTime=time.time() - startTime
    return diffTime

def main():
    # Setup pi
    GPIO.setmode(GPIO.BCM)
    
    pin_in = 17
    pin_out  = 13


    GPIO.setup(pin_out, GPIO.OUT)
    # Initialise output voltage to zero.
    GPIO.output(pin_out, GPIO.LOW)
    
    # When the output pin is low in the circuit, the input is pulled down to low
    GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    # Wait for the capacitor to discharge
    print "Waiting for capacitor to discharge" 

    timeCharge = countToHigh(pin_in, pin_out);

    timeConstant = timeCharge/math.log(2);
    print "Time constant: " + str(round(timeConstant*1000,1)) + "ms."
    C = 10e-6; #[F]
    R = timeConstant / C;

    # Use Steinhart and Hart Equation to calculate temperature
    A = 3.354016E-03;
    B = 2.569850E-04;
    C = 2.620131E-06;
    D = 6.383091E-08;
    R_ref = 10000;

    lr = math.log(R/R_ref);
    inverseOfT = A + B * lr + C * math.pow(lr,2) + D * math.pow(lr,3);

    T = 1/inverseOfT;
    T_deg = T -273.15;

    print "R = " + str(round(R/1000,1)) + "kOhm"
    print "Temperature = " + str(round(T_deg,1)) + " degC"

    print "wait for capacitor discharge"
    time.sleep(5 * timeConstant);
    GPIO.output(pin_out, GPIO.LOW)
    print "goodbye"

try:
    main()
finally:
	GPIO.cleanup()