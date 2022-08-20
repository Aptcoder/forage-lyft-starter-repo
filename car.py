from abc import ABC, abstractmethod

from .engine.engine_interface import Engine

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    def __init__(self, engine: Engine, last_service_date):
        self.last_service_date = last_service_date
        self.engine = engine

    def needs_service(self):
        pass


