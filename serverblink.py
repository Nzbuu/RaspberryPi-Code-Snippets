#!/usr/bin/env python

import RPi.GPIO as GPIO
from bottle import route, run, static_file

GPIO.setmode(GPIO.BOARD) 

led = 11

GPIO.setup(led, GPIO.OUT)


@route('/Off')
def uit():
	GPIO.output(led, False)
	return static_file('frownie.png', root = 'images', mimetype='image/png')

@route('/On')
def aan():
	GPIO.output(led, True)
	return static_file('smiley.png', root = 'images', mimetype='image/png')

try:
 run(host='0.0.0.0', port=8080, debug=True, reloader=True)
finally:
    GPIO.cleanup()