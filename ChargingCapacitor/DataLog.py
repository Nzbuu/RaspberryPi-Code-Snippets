import time
class DataLog:
    """ Class that performs data logging of sensor data """
    def __init__(self, sensor, measurementInterval):
        self.sensor = sensor;
        self.fileName = sensorID + ".txt";
        self.timeStep  = measurementInterval;    

    def recordMeasurement(self):

        measurement = self.sensor.getMeasurement();

    def writeMeasurementsToFile(self, measurements):
        f = open(self.fileName, 'w');
        
        data = [x.data for x in measurements];
        time = [x.timeStamp for x in measurements];

        # TODO: write all measurements to file and close the file


    #TODO: 
          # function that records an array of measurements and decides after a number of measurements to update the file