import decimal
import uuid
from datetime import date
from typing import List

from model.Car import Car
from model.CarClass import CarClass
from model.Driver import Driver
from model.Engine import Engine
from model.EngineCompanies import EngineCompanies
from model.Lorry import Lorry


class CarRepositories:
    _cars: List[Car] = []

    def add_car(self, car: Car) -> None:
        self._cars.append(car)

    def delete_car(self, search_id: uuid) -> None:
        c = next((c for c in self._cars if c.id == search_id), None)
        self._cars.remove(c)

    def check_existence_of_car(self, search_id: uuid) -> bool:
        c = next((c for c in self._cars if c.id == search_id), None)
        return c is not None

    @property
    def cars(self) -> List[Car]:
        return self._cars
# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# e = Engine(EngineCompanies.TOYOTA, 200)
# l = Lorry('Mers', CarClass.LORRY, decimal.Decimal(10020), d, e, 10, 1)
# c = Car('Mers', CarClass.REGULAR, decimal.Decimal(10020), d, e)
# cr = CarRepositories()
# cr.add_car(c)
# cr.add_car(l)
# print(cr.cars)