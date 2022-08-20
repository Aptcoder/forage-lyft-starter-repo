from .engine.sternman_engine import SternmanEngine

from .engine.willoughby_engine import WilloughbyEngine

from .engine.capulet_engine import CapuletEngine
from .engine.engine_interface import Engine
from .car import Car


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(capulet_engine, last_service_date)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(willoughby_engine, last_service_date)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        stenman_engine = SternmanEngine(warning_light_on)
        return Car(stenman_engine, last_service_date)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(willoughby_engine, last_service_date)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(capulet_engine, last_service_date)