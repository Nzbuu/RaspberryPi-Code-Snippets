__author__ = 'DRIA'
import sqlite3
import json
from Measurement import Measurement


class DataBase:
    """ Class handles writing and reading to database """

    def __init__(self, db_name):
        # Connect to database
        self.db = sqlite3.connect(db_name)

    def __del__(self):
        self.db.close()

    def create_database_table(self, table_name, **kwargs):
        # Expected input format:
        # create_database_table(data, time = 'REAL', value = 'REAL')
        #TODO: check if table already exists. Don't allow creating an existing table
        cursor = self.db.cursor()

        sql_str = 'CREATE TABLE ' + table_name + _assemble_create_args(**kwargs)

        cursor.execute(sql_str)
        cursor.close()
        self.db.commit()

    def write_measurement_to_database(self, measurement, table_name):
        # This function writes to the db
        # TODO: check if the table exists before trying to insert data into it
        meas = Measurement.convert_to_dict(measurement)

        list_of_keys = meas.keys()
        list_of_values = [meas[key] for key in list_of_keys]

        sql_str = 'INSERT INTO  ' + table_name + ' ' + _assemble_insert_args(meas)

        cursor = self.db.cursor()
        cursor.execute(sql_str, list_of_values)
        cursor.close()

        self.db.commit()

    def write_array_of_measurements_to_database(self, measurements, table_name):
        for measurement in measurements:
            self.write_measurement_to_database(measurement, table_name)

    def read_from_database(self, table_name):
        # This function reads from the db. Currently returns all data. TODO: Should in future be more specific.
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM ' + table_name)

        result = cursor.fetchall()
        cursor.close()
        return result


def _assemble_insert_args(measurement):
    # expected output for measurement '(timeStamp, values, units) VALUES(?,?,?)'
    list_of_keys = measurement.keys()
    keys = ','.join(list_of_keys)

    # make list of question marks the size of the length of the list of keys
    question_mark_list_length = len(list_of_keys)
    qm_list = ','.join(['?' for x in range(0, question_mark_list_length)])

    string_out = '(' + keys + ')' + ' VALUES (' + qm_list + ')'
    return string_out


def _assemble_create_args(**kwargs):
    table_contents = '{keyName} {valueName}'
    table_contents = [table_contents.format(keyName=key, valueName=kwargs[key]) for key in kwargs]

    string_out = '(' + ','.join(table_contents) + ')'
    return string_out