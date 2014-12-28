from unittest import TestCase
from DataBase import DataBase
from Measurement import Measurement

__author__ = 'Anniek'


class TestDataBase(TestCase):
    def test_create_database_table(self):
        o = DataBase('testDB')
        o.create_database_table('data', timeStamp='REAL', value='REAL', units='TEXT')
        # TODO: insert assertion

    def test_write_measurement_to_database(self):
        o = DataBase('testDB')
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        o.write_measurement_to_database(data_point, 'data')
        # TODO: insert assertion

    def test_read_from_database(self):
        o = DataBase('testDB')
        results = o.read_from_database('data')
        # TODO: insert assertion

    def test_write_array_of_measurements_to_database(self):
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        array_of_points = [data_point, data_point, data_point]
        o = DataBase('testDB')

        o.write_array_of_measurements_to_database(array_of_points, 'data')
        # TODO: insert assertion