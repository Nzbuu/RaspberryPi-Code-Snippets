import webiopi
import RPi.GPIO as GPIO

#Enable debug output
webiopi.setDebug()

GPIO.setmode(GPIO.BOARD) 

led = 11

# Define GPIO functions

@webiopi.macro
def led_on():
    webiopi.debug("Running returnWebsite_withWebIoPi - led_on")
    GPIO.output(led, GPIO.HIGH)


@webiopi.macro
def led_off():
    webiopi.debug("Running returnWebsite_withWebIoPi - led_off")
    GPIO.output(led, GPIO.LOW)

# Called by WebIoPi at script loading
def setup():
    webiopi.debug("returnWebsite_withWebIoPi - setup")
    GPIO.setup(led, GPIO.OUT)

# Called by WebIoPi at server shutdown
def destroy():
    webiopi.debug("returnWebsite_withWebIoPi - destroy")
    GPIO.setup(led, GPIO.IN)    

