from datetime import timedelta, datetime
import unittest
from battery.splinder_battery import SplinderBattery
from engine.capulet_engine import CapuletEngine

from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestSplinder(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=1500)

        engine = SplinderBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=150)

        engine = SplinderBattery(last_service_date)
        self.assertFalse(engine.needs_service())

class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=1000)

        engine = SplinderBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today() - timedelta(days=150)

        engine = SplinderBattery(last_service_date)
        self.assertFalse(engine.needs_service())



if __name__ == '__main__':
    unittest.main()
