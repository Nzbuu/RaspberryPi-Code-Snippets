__author__ = 'DRIA'
from unittest import TestCase
import os.path
from DataBase import DataBase
import json
from measurement import Measurement
import time


db = DataBase('DB/SensorData')

table_list = db.list_all_tables_in_db
results = db.read_from_database('DS18B20')

measurements = json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))