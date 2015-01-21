from PeriodicTimer import PeriodicTimer
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
        self.db = DataBase('DB/SensorData')

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
        # todo: make it automatic what table columns are supposed to be there, derived from contents of measurement object?
        self.db.create_database_table(self.table_name, timeStamp='REAL', value='REAL', units='TEXT')

        timerDataAquisition = PeriodicTimer(self.timeStep, self.appendMeasurement)
        timerWriteToFile = PeriodicTimer(self.writeInterval, self.writeMeasurementsToDatabase)

        timerDataAquisition.start()
        time.sleep(1)
        timerWriteToFile.start()

        try:
            while True:
                pass

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
            self.db.write_array_of_measurements_to_database(writeData, self.table_name)

        return True