from bottle import get, put, route, run, static_file, debug, request, response
import json
import sys
import os
sys.path.append(os.path.realpath('../Sensors'))

from DataBase import DataBase


#enable bottle debug
debug(True)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='.')

@get('/data')
def getData():
    db = DataBase('../Sensors/DB/SensorData')
    results = db.read_from_database('DS18B20', 5000, 'timeStamp') # limit to 96 data points for now

    time = [row.timeStamp for row in results]
    value = [row.value for row in results]

    measurements = json.dumps({'time': time, 'values':value })

    return measurements

try:
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
finally:
    print "Bye!"
