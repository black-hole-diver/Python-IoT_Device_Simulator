from datetime import datetime
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from dashboard import Dashboard

class Device:
    def __init__(self, sensor_id, url, duration, dashboard):
        self.sensor = Sensor(sensor_id)
        self.processor = DataProcessor()
        self.communication = Communication(url)
        self.duration = duration
        self.dashboard = dashboard

    def run(self):
        start_time = datetime.now()
        while (datetime.now() - start_time).total_seconds() < self.duration:
            sensor_reading = self.sensor.get_reading()
            self.processor.process_data(sensor_reading)
            try:
                self.communication.send_data(sensor_reading)
            except Exception as e:
                print('Error while sending data:', e)
            if (datetime.now() - sensor_reading['timestamp']).total_seconds():
                self.dashboard.update(sensor_reading)