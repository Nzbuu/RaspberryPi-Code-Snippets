__author__ = 'DRIA'
import sqlite3
import json


class DataBase:
    """ Class handles writing and reading to database """

    def __init__(self, db_name):
        # Connect to database
        self.db = sqlite3.connect(db_name)

    def __del__(self):
        self.db.close()

    def create_database_table(self, table_name, **kwargs):
        # Expected input format:
        #create_database_table(time = 'REAL', value = 'REAL')

        cursor = self.db.cursor()

        sql_str = 'CREATE TABLE ' + table_name + _assemble_create_args(kwargs)

        cursor.execute(sql_str)
        cursor.close()
        self.db.commit()

    def write_measurement_to_database(self, measurement, table_name):
        # This function writes to the db
        # the format of measurement is expected be a dictionary, e.g.
        # measurement = {'temperature':20, 'time': 10201}

        # TODO: check if the table exists before trying to insert data into it

        list_of_keys = measurement.keys()
        list_of_values = [measurement[key] for key in list_of_keys]

        sql_str = 'INSERT INTO  ' + table_name + _assemble_insert_args(measurement)

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
    # example measurement = {'temperature':20, time: 10201, 'humidity': 67%}
    # expected output for measurement '(time, temperature, humidity) VALUES(?,?,?)'
    list_of_keys = measurement.keys()
    list_of_values = [measurement[key] for key in list_of_keys]

    keys = ','.join(list_of_keys)

    # make list of question marks the size of the length of the list of keys
    question_mark_list_length = len(list_of_keys)
    qm_list = ','.join(['?' for x in range(0,question_mark_list_length)])

    string_out = '(' + keys + ')' + ' VALUES (' + qm_list + ')'

    return string_out


def _assemble_create_args(input_dict):

    table_contents = '{keyName} {valueName}'
    table_contents = [table_contents.format(keyName=key, valueName=input_dict[key]) for key in input_dict]

    string_out = '('
    for item in table_contents:
        string_out += item + ', '

    # remove trailing comma
    string_out = string_out[0:len(string_out)-2]
    # close brackets
    string_out += ')'

    return string_out

def _format_measurement(self, measurement):
    # measurement = {'temperature':20, 'time': 10201, 'units':units}
    measurement['time'] = measurement.time;
    # TODO: finish this




