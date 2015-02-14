from unittest import TestCase
import os.path
from DataBase import DataBase
from measurement import Measurement

__author__ = 'Anniek'


class TestDataBase(TestCase):
    def test_create_database_table(self):
        file_path = 'DB/Dummy'
        o = DataBase(file_path)
        o.create_database_table('Dummy', timeStamp='REAL', value='REAL', units='TEXT')
        # check if db has been created
        os.path.isfile(file_path)

        # check if table has been created
        tables = o.list_all_tables_in_db()
        self.assertEqual(tables, ['Dummy'])

    def test_write_measurement_to_database(self):
        o = DataBase('DB/Dummy')
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        o.write_measurement_to_database(data_point, 'Dummy')

    def test_read_from_database(self):
        # check if the measurement has been written to the db correctly
        o = DataBase('DB/Dummy')
        results = o.read_from_database('Dummy', 3)
        self.assertTrue(len(results) > 0)
        self.assertEqual(len(results), 3)

    def test_write_array_of_measurements_to_database(self):
        data_point = Measurement(value=20, timeStamp=10201, units='degC')
        array_of_points = [data_point, data_point, data_point]
        o = DataBase('DB/Dummy')

        o.write_array_of_measurements_to_database(array_of_points, 'Dummy')
        # TODO: insert assertion