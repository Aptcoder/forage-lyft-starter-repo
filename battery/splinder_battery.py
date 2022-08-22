from datetime import datetime, timedelta
from battery.battery_interface import Battery


class SplinderBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        three_years_ago = datetime.today() - timedelta(days=1095)
        return self.last_service_date < three_years_ago