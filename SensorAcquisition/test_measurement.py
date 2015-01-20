from unittest import TestCase
from measurement import Measurement
__author__ = 'Anniek'


class TestMeasurement(TestCase):
    def test_convert_to_dict(self):
        m = Measurement(timeStamp=1, value=2, units='degC')
        outputs = m.convert_to_dict()
        self.assertDictEqual(outputs, {'timeStamp': 1, 'value': 2, 'units': 'degC'})

