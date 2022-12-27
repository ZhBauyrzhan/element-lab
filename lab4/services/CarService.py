import uuid
from typing import List

from exceptions.CarAlreadyExistsError import CarAlreadyExistsError
from exceptions.NoSuchCarError import NoSuchCarError
from model.Car import Car
from repositories.CarRepositories import CarRepositories


class CarService:
    _repository: CarRepositories

    def __init__(self, repository: CarRepositories):
        self._repository = repository

    def create_car(self, car: Car) -> None:
        if not self._repository.check_existence_of_car(car.id):
            self._repository.add_car(car)
        else:
            raise CarAlreadyExistsError

    def delete_car(self, search_id: uuid) -> None:
        if self._repository.check_existence_of_car(search_id):
            self._repository.delete_car(search_id)
        else:
            raise NoSuchCarError

    def get_cars(self) -> List[Car]:
        return self._repository.cars
