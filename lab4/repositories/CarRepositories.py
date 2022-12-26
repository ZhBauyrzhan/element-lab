import decimal
import uuid
from typing import List

from model.Car import Car
from model.CarClass import CarClass
from model.Driver import Driver
from model.Engine import Engine


class CarRepositories:
    _cars: List[Car] = []

    def add_car(self, car_brand: str, car_class: CarClass,
                weight: decimal.Decimal, driver: Driver, engine: Engine) -> None:
        self._cars.append(Car(car_brand, car_class, weight, driver, engine))

    def delete_car(self, search_id: uuid) -> None:
        c = next((c for c in self._cars if c.id == search_id), None)
        self._cars.remove(c)

    def check_existence_of_car(self, search_id: uuid) -> bool:
        c = next((c for c in self._cars if c.id == search_id), None)
        return c is not None

    @property
    def cars(self) -> List[Car]:
        return self._cars
