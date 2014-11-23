from bottle import route, run, static_file, debug, request, response
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

@route('/test')
def aan():
    return "test"    

@route('/Off')
def uit():
	GPIO.output(led, False)

@route('/On')
def aan():
	GPIO.output(led, True)

@route('/SetStatus', method='POST')
def setStatus():
    print "POST Header : \n %s" % dict(request.json) #for debug header

    data = request.json;
    status  = data['LedStatus']

    global LedStatus
    LedStatus = status
    print "LedStatus : \n %s" % str(LedStatus)

    GPIO.output(led, LedStatus)

@route('/GetStatus')
def getStatus():
    
    # Use this if the global variable set in setStatus should be used
    #return { "LedStatus" : str(LedStatus)}
    
    # determines the state from the raspberry pi pin
    state = GPIO.input(led)
    return { "LedStatus" : str(state)}

try:
 run(host='0.0.0.0', port=8080, debug=True, reloader=True)
finally:
    GPIO.cleanup()
