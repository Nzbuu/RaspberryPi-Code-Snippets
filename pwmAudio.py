import RPi.GPIO as GPIO
import time

def main():
   # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)
    # set up GPIO output channel
    pin_number = 12
    
    GPIO.setup(pin_number, GPIO.OUT)
    
    p = GPIO.PWM(pin_number, 1000.0)
    p.start(50.0)
    time.sleep(1)
    
    p.ChangeFrequency(400.0)
    time.sleep(1)
    
    p.stop()
    
try:
    main()
    
finally:
    GPIO.cleanup()
