from bottle import get, put, route, run, static_file, debug, request, response
import RPi.GPIO as GPIO
import json

# Create global variable for LED status and initialise to false
LedStatus = False

#enable bottle debug
debug(True)

GPIO.setmode(GPIO.BOARD) 

led = 11

GPIO.setup(led, GPIO.OUT)

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='webpageFiles')

@put('/status')
def setStatus():
    print "PUT Header : \n %s" % dict(request.json) #for debug header

    data = request.json;
    status  = data['LedStatus']

    LedStatus = status
    print "LedStatus : \n %s" % str(LedStatus)

    GPIO.output(led, LedStatus)

@get('/status')
def getStatus():
    # Use this if the global variable set in setStatus should be used
    #return { "LedStatus" : str(LedStatus)}
    
    # determines the state from the raspberry pi pin
    state = GPIO.input(led)

    #TODO: send current time in return JSON
    now = datetime.datetime.now()
    return { "LedStatus" : str(state)}

try:
 run(host='0.0.0.0', port=8080, debug=True, reloader=True)
finally:
    GPIO.cleanup()
