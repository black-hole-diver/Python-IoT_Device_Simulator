import random
from datetime import datetime, timedelta

class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def get_reading(self):
        reading = random.uniform(0, 100)
        timestamp = datetime.now()
        return {'sensor_id': self.sensor_id, 'reading': reading, 'timestamp': timestamp}