from datetime import date
from typing import List

from model.Driver import Driver


class DriverRepositories:
    _drivers: List[Driver] = []

    def add_driver(self, driver: Driver) -> None:
        self._drivers.append(driver)

    def delete_driver(self, full_name: str) -> None:
        driver = next(d for d in self._drivers if d.full_name == full_name)
        self._drivers.remove(driver)

    def check_existence_of_driver(self, full_name: str) -> bool:
        d = next((d for d in self._drivers if d.full_name == full_name), None)
        return d is not None

    @property
    def drivers(self) -> List[Driver]:
        return self._drivers
