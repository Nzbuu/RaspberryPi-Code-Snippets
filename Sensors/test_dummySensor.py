import time
from unittest import TestCase
from DummySensor import DummySensor

__author__ = 'dria'


class TestDummySensor(TestCase):
    def test_getMeasurement(self):
        s = DummySensor()
        time_now = time.time()
        measurement = s.getMeasurement()
        self.assertEqual(measurement.value, 1)
        self.assertEqual(measurement.units, "-")
        self.assertEqual(measurement.timeStamp, time_now)