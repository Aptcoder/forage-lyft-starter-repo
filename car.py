from abc import ABC, abstractmethod

from battery.battery_interface import Battery
from tyre.tyre_interface import Tyre

from .engine.engine_interface import Engine

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tyre: Tyre, last_service_date):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service()


