import time


class DummySensor:
    """ Dummy Sensor """
    # Class variable: Sensor type
    def __init__(self):
        pass

    sensorType = "DummySensor"
    sensorID = "Dummy"
    sensorUnits = "-"

    def getMeasurement(self):
        class Measurement(object):
            def __init__(self):
                pass
            timeStamp = 0
            data = 0
            units = ""

        newMeasurement = Measurement()
        newMeasurement.timeStamp = time.time()
        newMeasurement.data = 1
        newMeasurement.units = self.sensorUnits
        return newMeasurement
