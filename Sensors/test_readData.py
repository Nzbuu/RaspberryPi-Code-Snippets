__author__ = 'DRIA'
import sys
import os
sys.path.append(os.path.realpath('../SensorAcquisition'))
from DataBase import DataBase

db = DataBase('../SensorAcquisition/DB/SensorData')
results = db.read_from_database('DS18B20', 5000) # limit to 96 data points for now

time = [row.timeStamp for row in results]
value = [row.value for row in results]

measurements = json.dumps({'time': time, 'values':value })