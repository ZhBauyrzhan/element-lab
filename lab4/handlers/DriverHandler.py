from datetime import date
from typing import List

from exceptions import DriverAlreadyExistsError
from exceptions.NoSuchDriverError import NoSuchDriverError
from exceptions.TooYoungError import TooYoungError
from model.Driver import Driver
from services.DriverService import DriverService


class DriverHandler:
    def __init__(self, service: DriverService):
        self._service = service

    def create_drive(self, name: str, surname: str, age: int,
                     started_driver_date: date) -> str:
        try:
            if age < 18:
                raise TooYoungError
            self._service.create_driver(Driver(name, surname, age, started_driver_date))
            return f'Successfully created driver'
        except DriverAlreadyExistsError:
            return f'Driver already exists error'

    def delete_drive(self, full_name: str) -> str:
        try:
            self._service.delete_drive(full_name)
            return f'Driver was deleted successfully'
        except NoSuchDriverError:
            return f'No such driver with this full name'

    def get_driver(self) -> List[Driver]:
        return self._service.get_driver()

    def get_driver_by_full_name(self, full_name: str) -> Driver:
        driver = next((d for d in self._service.get_driver() if d.full_name == full_name), None)
        return driver
