import PeriodicTimer
import time
from DataBase import DataBase


class DataLog:
    """ Class that performs data logging of sensor data """

    def __init__(self, sensor, measurementInterval, writeInterval):
        self.sensor = sensor
        self.timeStep = measurementInterval
        self.writeInterval = writeInterval
        self.measurements = []
        self.table_name = sensor.sensorID
        self.db = DataBase('SensorData')

    def recordSingleMeasurement(self):
        measurement = self.sensor.getMeasurement()
        return measurement

    def appendMeasurement(self):
        measurement = self.recordSingleMeasurement()
        self.measurements.append(measurement)
        return True

    def clearMeasurements(self):
        self.measurements = []

    def run(self):
        timerDataAquisition = PeriodicTimer.PeriodicTimer(self.timeStep, self.appendMeasurement)
        timerWriteToFile = PeriodicTimer.PeriodicTimer(self.writeInterval, self.writeMeasurementsToDatabase())

        timerDataAquisition.start()
        time.sleep(1)
        timerWriteToFile.start()

        try:
            while True:
                time.sleep(1)

        finally:
            self.writeMeasurementsToDatabase()
            timerDataAquisition.cancel()
            timerWriteToFile.cancel()

    def writeMeasurementsToDatabase(self):

        writeData = self.measurements

        if not writeData:
            pass
        else:
            self.clearMeasurements()
            # Write data to db
            self.db.write_array_of_data_points_to_database(writeData, self.table_name)

        return True