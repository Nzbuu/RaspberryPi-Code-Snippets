from bottle import route, run, static_file
import RPi.GPIO as GPIO


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

try:
 run(host='0.0.0.0', port=8080, debug=True, reloader=True)
finally:
    GPIO.cleanup()
