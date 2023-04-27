import random
from datetime import datetime, timedelta
import statistics
import matplotlib.pyplot as plt

class Dashboard:
    def __init__(self):
        self.fig, self.axs = plt.subplots(3, 1)
        self.readings = []
        self.means = []
        self.medians = []
        self.stdevs = []
        self.timer = datetime.now()

    def update(self, sensor_reading):
        self.readings.append(sensor_reading)
        self.means.append(sensor_reading['reading'])
        self.medians.append(sensor_reading['reading'])
        self.stdevs.append(sensor_reading['reading'])
        self.timer = datetime.now()
        self.plot()

    def plot(self):
        try:
            #plt.switch_backend('TkAgg')
            plt.show(block=False)
            #plt.clf()
            recent_readings = [reading for reading in self.readings if (self.timer - reading['timestamp']).total_seconds() < 10]
            self.axs[0].plot([reading['timestamp'] for reading in recent_readings], [reading['reading'] for reading in recent_readings])
            self.axs[0].set_ylabel('Reading')
            recent_means = self.means[-len(recent_readings):]
            self.axs[1].plot([reading['timestamp'] for reading in recent_readings], recent_means)
            self.axs[1].set_ylabel('Mean')

            recent_medians = self.medians[-len(recent_readings):]
            self.axs[2].plot([reading['timestamp'] for reading in recent_readings], recent_medians)
            recent_stdevs = self.stdevs[-len(recent_readings):]
            self.axs[2].plot([reading['timestamp'] for reading in recent_readings], recent_stdevs)
            self.axs[2].set_ylabel('Median/Stdev')
            self.axs[2].set_xlabel('Time')

            plt.pause(0.01)
        except Exception as e:
            print('Error while updating dashboard:', e)
