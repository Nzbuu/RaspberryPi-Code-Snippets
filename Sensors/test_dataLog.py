import time
from unittest import TestCase
from DataLog import DataLog
from DummySensor import DummySensor

__author__ = 'dria'


class TestDataLog(TestCase):
    def test_recordSingleMeasurement(self):
        sensor = DummySensor()
        t1 = 5
        t2 = 100
        d = DataLog(sensor, t1, t2)
        measurement = d.recordSingleMeasurement()
        time_now = time.time()
        self.assertEqual(measurement.value, 1)
        self.assertEqual(measurement.units, "-")
        self.assertEqual(measurement.timeStamp, time_now)


    def test_appendMeasurement(self):
        sensor = DummySensor()
        t1 = 5
        t2 = 100
        d = DataLog(sensor, t1, t2)
        d.appendMeasurement()
        d.appendMeasurement()
        d.appendMeasurement()
        measurements = d.measurements
        self.assertEqual(len(measurements), 3)

    def test_writeMeasurementsToDatabase(self):
        sensor = DummySensor()
        t1 = 5
        t2 = 100
        d = DataLog(sensor, t1, t2)
        d.appendMeasurement()
        d.appendMeasurement()
        d.appendMeasurement()
        d.writeMeasurementsToDatabase()
        d.appendMeasurement()
        d.appendMeasurement()
        d.writeMeasurementsToDatabase()
        # TODO: Add assertion statement

    def test_clearMeasurements(self):
        sensor = DummySensor()
        t1 = 5
        t2 = 100
        d = DataLog(sensor, t1, t2)
        d.appendMeasurement()
        d.appendMeasurement()
        d.appendMeasurement()
        d.clearMeasurements()
        measurements = d.measurements
        self.assertEqual(measurements, [])

