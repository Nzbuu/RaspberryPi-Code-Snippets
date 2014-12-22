from unittest import TestCase
from DataBase import DataBas
from measurement import measurement

__author__ = 'Anniek'


class TestDataBase(TestCase):
    def test_create_database_table(self):
        o = DataBase('testDB')
        o.create_database_table('data', time='REAL', temperature='REAL', humidity='REAL')
        # TODO: insert assertion

    def test_write_measurement_to_database(self):
        o = DataBase('testDB')
        #todo: use measurement class
        data_point = {'temperature': 20, 'time': 10201, 'humidity': 67}
        o.write_measurement_to_database(data_point, 'data')
        # TODO: insert assertion

    def test_read_from_database(self):
        o = DataBase('testDB')
        results = o.read_from_database('data')
        # TODO: insert assertion

    def write_array_of_measurements_to_database(self):
        #todo: use measurement class
        data_point = {'temperature': 20, 'time': 10201, 'humidity': 67}
        array_of_points = [data_point, data_point, data_point]
        o = DataBase('testDB')

        o.write_array_of_measurements_to_database(array_of_points, 'data')
        # TODO: insert assertion