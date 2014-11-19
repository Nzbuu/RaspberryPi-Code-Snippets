import RPi.GPIO as GPIO  
import time  
# blinking function  
def blink(pin, ratio=0.5):
        ratio = 0 if ratio < 0 else ratio
        ratio = 1 if ratio > 1 else ratio

        time_on = 1 * ratio
        time_off = 1 * (1 - ratio)

        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(time_on)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(time_off)  
        return  

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel
pin_number = 11

GPIO.setup(pin_number, GPIO.OUT)  
# blink GPIO17 50 times  
try:
    for i in range(0, 20):  
        blink(pin_number, 0.75)

finally:
    GPIO.cleanup()
