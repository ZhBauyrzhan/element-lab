import decimal
import uuid
from abc import ABC
from dataclasses import dataclass, field
from datetime import date

from model.CarClass import CarClass
from model.Driver import Driver
from model.Engine import Engine
from model.EngineCompanies import EngineCompanies


@dataclass
class Car(ABC):
    id: uuid = field(init=False)
    _car_brand: str
    _car_class: CarClass
    weight: decimal.Decimal
    _driver: Driver
    _engine: Engine

    def __post_init__(self):
        self.id = uuid.uuid4()

    def start(self) -> None:
        print('Start')

    def stop(self) -> None:
        print('Stop')

    def turn_right(self) -> None:
        print('Turn right')

    def turn_left(self) -> None:
        print('Turn left')

    @property
    def driver(self) -> Driver:
        return self._driver

    @property
    def car_brand(self) -> str:
        return self._car_brand

    @property
    def car_driver(self) -> Driver:
        return self._driver

    @property
    def car_class(self) -> CarClass:
        return self._car_class

    @property
    def engine(self) -> Engine:
        return self._engine

    def __str__(self) -> str:
        return f'id: {self.id} \n brand: {self.car_brand} \n class: {self.car_class} \n weight: {self.weight} \n driver: {self.car_driver} \n ' \
               f'engine: {self.engine}'

# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# e = Engine(EngineCompanies.TOYOTA,200)
# c = Car('Mers', CarClass.REGULAR, decimal.Decimal(10020), d, e)
# print(c)