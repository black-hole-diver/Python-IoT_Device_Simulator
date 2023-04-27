import statistics

class DataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self, sensor_reading):
        self.data.append(sensor_reading)

    def get_stats(self):
        readings = [reading['reading'] for reading in self.data]
        return {'mean': statistics.mean(readings), 'median': statistics.median(readings), 'stdev': statistics.stdev(readings)}

