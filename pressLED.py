import RPi.GPIO as GPIO  
import time  

def main():
    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)
    
    # set up GPIO output channel
    output_pin = 11
    GPIO.setup(output_pin, GPIO.OUT)
    
    state_led = False
    GPIO.output(output_pin, state_led)
    
    # set up GPIO input channel
    input_pin = 13
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    GPIO.add_event_detect(input_pin, GPIO.RISING, bouncetime=200)
    
    while True:
        time.sleep(0.01)
        
        if GPIO.event_detected(input_pin):
            print('Trigger')
            state_led = not state_led
            GPIO.output(output_pin, state_led)

try:
    main()
    
finally:
    GPIO.cleanup()
