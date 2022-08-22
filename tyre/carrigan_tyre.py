from datetime import datetime, timedelta
from .tyre_interface import Tyre


class CarriganTyre(Tyre):
    def __init__(self, tires_values: list):
        self.tires_values = tires_values

    def needs_service(self):
        for value in self.tires_values:
            if float(value) >= 0.9:
                return True
            
        return False
