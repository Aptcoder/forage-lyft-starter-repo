from datetime import timedelta, datetime
import unittest
import battery
from battery.splinder_battery import SplinderBattery
from battery.nubblin_battery import NubblinBattery
from engine.capulet_engine import CapuletEngine



class TestSplinder(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=1500)

        battery = SplinderBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=740)

        battery = SplinderBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=1500)

        battery = NubblinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=150)

        battery = NubblinBattery(last_service_date)
        self.assertFalse(battery.needs_service())



if __name__ == '__main__':
    unittest.main()
