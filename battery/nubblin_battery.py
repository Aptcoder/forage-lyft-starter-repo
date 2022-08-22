from datetime import datetime, timedelta
from battery.battery_interface import Battery


class NubblinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        four_years_ago = datetime.today() - timedelta(days=1460)
        return self.last_service_date < four_years_ago