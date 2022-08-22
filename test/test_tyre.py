import unittest

from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre
from tyre.tyre_interface import Tyre


class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):
        tires_values = [0.2, 0.3, 0.7, 1]

        tyre = CarriganTyre(tires_values)
        self.assertTrue(tyre.needs_service())

    def test_should_not_serviced(self):
        tires_values = [0.2, 0.3, 0.7, 0.3]

        tyre = CarriganTyre(tires_values)
        self.assertFalse(tyre.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self):
        tires_values = [0.9, 0.5, 0.8, 0.9]

        tyre: Tyre = OctoprimeTyre(tires_values)
        self.assertTrue(tyre.needs_service())

    def test_should_not_be_serviced(self):
        tires_values = [0.3, 0.4, 0.2, 0.1]

        tyre: Tyre = OctoprimeTyre(tires_values)
        self.assertFalse(tyre.needs_service())

if __name__ == '__main__':
    unittest.main()