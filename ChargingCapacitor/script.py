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
    print "Time constant: " + str(timeConstant) + "s."
    C = 10e-6; #[F]
    R = timeConstant / C;

    print "R = " + str(R/1000) + "kOhm"

    print "wait for capacitor discharge"
    time.sleep(5 * timeConstant);
    GPIO.output(pin_out, GPIO.LOW)
    print "goodbye"

try:
    main()
finally:
	GPIO.cleanup()