__author__ = 'Anniek'


class Measurement(object):
    def __init__(self, **kwargs):
        # Todo: intialise to default values if no inputs are given
        self.timeStamp = kwargs['timeStamp']
        self.data = kwargs['data']
        self.units = kwargs['units']

    def set_values(self, timeStamp, data, units):
        self.timeStamp = timeStamp
        self.data = data
        self.units = units

    def convert_to_dict(self):
        measurement_dict = {'timeStamp' : self.timeStamp, 'data' : self.data, 'units' : self.units}
        return measurement_dict


