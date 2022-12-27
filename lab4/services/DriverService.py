from typing import List

from exceptions import DriverAlreadyExistsError
from exceptions.NoSuchDriverError import NoSuchDriverError
from model.Driver import Driver
from repositories.DriverRepositories import DriverRepositories
from repositories.PersonRepositories import PersonRepositories


class DriverService:
    _repository: DriverRepositories

    def __init__(self, driver_repository: DriverRepositories, ):
        self._repository = driver_repository

    def create_driver(self, driver: Driver) -> None:
        if not self._repository.check_existence_of_driver(driver.full_name):
            self._repository.add_driver(driver)
        else:
            raise DriverAlreadyExistsError

    def delete_drive(self, full_name) -> None:
        if self._repository.check_existence_of_driver(full_name):
            self._repository.delete_driver(full_name)
        else:
            raise NoSuchDriverError

    def get_driver(self) -> List[Driver]:
        return self._repository.drivers
