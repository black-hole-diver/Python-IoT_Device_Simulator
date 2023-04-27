import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

from sensor import Sensor
from communication import Communication
from dashboard import Dashboard
from data_processor import DataProcessor
from device import Device

import matplotlib.pyplot as plt
import numpy as np

class TestSensor(unittest.TestCase):

    def test_get_reading(self):
        sensor = Sensor('sensor1')
        reading = sensor.get_reading()
        self.assertEqual(reading['sensor_id'], 'sensor1')
        self.assertTrue(0 <= reading['reading'] <= 100)
        self.assertIsInstance(reading['timestamp'], datetime)


class TestDataProcessor(unittest.TestCase):

    def test_process_data(self):
        processor = DataProcessor()
        processor.process_data({'sensor_id': 'sensor1', 'reading': 50, 'timestamp': datetime.now()})
        self.assertEqual(len(processor.data), 1)
        self.assertEqual(processor.data[0]['reading'], 50)

    def test_get_stats(self):
        processor = DataProcessor()
        processor.data = [{'sensor_id': 'sensor1', 'reading': 50, 'timestamp': datetime.now()},
                          {'sensor_id': 'sensor1', 'reading': 60, 'timestamp': datetime.now()},
                          {'sensor_id': 'sensor1', 'reading': 70, 'timestamp': datetime.now()}]
        stats = processor.get_stats()
        self.assertEqual(stats['mean'], 60)
        self.assertEqual(stats['median'], 60)

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.dashboard = Dashboard()

    def test_plot(self):
        timestamp = datetime.now()
        recent_readings = [{'sensor_id': 'sensor1', 'reading': 50, 'timestamp': timestamp},
                           {'sensor_id': 'sensor1', 'reading': 60, 'timestamp': timestamp + timedelta(seconds=5)}]
        self.dashboard.readings = recent_readings
        self.dashboard.means = [50, 60]
        self.dashboard.medians = [50, 60]
        self.dashboard.stdevs = [50, 60]

        with patch.object(plt, 'show'), patch.object(plt, 'pause'):
            self.dashboard.plot()

        self.assertEqual(self.dashboard.axs[0].get_ylabel(), 'Reading')
        self.assertEqual(self.dashboard.axs[1].get_ylabel(), 'Mean')
        self.assertEqual(self.dashboard.axs[2].get_ylabel(), 'Median/Stdev')
        self.assertEqual(self.dashboard.axs[2].get_xlabel(), 'Time')

class TestCommunication(unittest.TestCase):

    @patch('builtins.print')
    def test_send_data_success(self, mock_print):
        communication = Communication('https://google.com')
        communication.send_data({'sensor_id': 'sensor1', 'reading': 50, 'timestamp': '2022-04-27 09:30:00'})
        mock_print.assert_called_once_with('Sending data:', {'sensor_id': 'sensor1', 'reading': 50, 'timestamp': '2022-04-27 09:30:00'}, 'to', 'https://google.com')