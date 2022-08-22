from .tyre_interface import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, tires_values: list):
        self.tires_values = tires_values

    def needs_service(self):
        return sum(self.tires_values) >= 3
