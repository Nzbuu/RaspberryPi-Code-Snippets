from unittest import TestCase
import os.path
from DataBase import DataBase
from Measurement import Measurement

__author__ = 'Anniek'


class TestDataBase(TestCase):
    def test_create_database_table(self):
        file_path = 'DB/testDB'
        o = DataBase(file_path)
        o.create_database_table('data', timeStamp='REAL', value='REAL', units='TEXT')
        # check if db has been created
        os.path.isfile(file_path)

        # check if table has been created
        tables = o.list_all_tables_in_db()
        self.assertEqual(tables, ['data'])

    def test_write_measurement_to_database(self):
        o = DataBase('DB/testDB')
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        o.write_measurement_to_database(data_point, 'data')

    def test_read_from_database(self):
        # check if the measurement has been written to the db correctly
        o = DataBase('DB/testDB')
        results = o.read_from_database('data')

    def test_write_array_of_measurements_to_database(self):
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        array_of_points = [data_point, data_point, data_point]
        o = DataBase('DB/testDB')

        o.write_array_of_measurements_to_database(array_of_points, 'data')
        # TODO: insert assertion