__author__ = 'DRIA'
import sqlite3
import json
from collections import namedtuple
from Measurement import Measurement


class DataBase:
    """ Class handles writing and reading to database """

    def __init__(self, db_name):
        # Connect to database (db is created if it does not exist)
        self.db = sqlite3.connect(db_name)
        self.db.row_factory = _named_tuple_factory

    def __del__(self):
        self.db.close()

    def create_database_table(self, table_name, **kwargs):
        # Expected input format:
        # create_database_table(data, time = 'REAL', value = 'REAL')
        cursor = self.db.cursor()

        sql_str = 'CREATE TABLE IF NOT EXISTS ' + table_name + _assemble_create_args(**kwargs)

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

        results_list = cursor.fetchall()
        cursor.close()
        # The functionality below will probably be moved to  a separate class
        # results_dict = named_tuple_list_to_dict(results_list)
        # results_json = json.dumps(results_dict, sort_keys=True, indent=4, separators=(',', ': '))
        return results_list

    def delete_table(self, table_name):
        cursor = self.db.cursor()
        cursor.execute('DROP TABLE ' + table_name)
        cursor.close()
        self.db.commit()

    def list_all_tables_in_db(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT name from sqlite_master WHERE type='table';")
        result = cursor.fetchall()
        result = [x[0] for x in result]
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


def _named_tuple_factory(cursor, row):
    field_names = [col[0] for col in cursor.description]
    Row = namedtuple("Row", field_names)
    return Row(*row)


def _named_tuple_to_dict(named_tuple):
    dictionary = {}
    for field in named_tuple._fields:
        dictionary[field] = getattr(named_tuple, field)

    return dictionary


def named_tuple_list_to_dict(named_tuple_list):
    list_out = []
    for tuple_item in named_tuple_list:
        list_out.append(_named_tuple_to_dict(tuple_item))

    return list_out