import PeriodicTimer
import time


class DataLog:
    """ Class that performs data logging of sensor data """

    def __init__(self, sensor, measurementInterval, writeInterval):
        self.sensor = sensor
        self.fileName = sensor.sensorID + ".txt"
        self.timeStep = measurementInterval
        self.writeInterval = writeInterval
        self.measurements = []

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
        timerWriteToFile = PeriodicTimer.PeriodicTimer(self.writeInterval, self.writeMeasurementsToFile)

        timerDataAquisition.start()
        time.sleep(1)
        timerWriteToFile.start()

        try:
            while True:
                time.sleep(1)

        finally:
            self.writeMeasurementsToFile()
            timerDataAquisition.cancel()
            timerWriteToFile.cancel()

    def writeMeasurementsToFile(self):
        # Copy
        writeData = self.measurements

        if not writeData:
            pass
        else:
            self.clearMeasurements()
            # Write data to file
            f = open(self.fileName, 'a')
            [f.write(str(m.timeStamp)+"\t"+str(m.data)+"\n") for m in writeData]
            f.close()

        return True