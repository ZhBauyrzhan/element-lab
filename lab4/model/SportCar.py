import decimal
from dataclasses import dataclass
from datetime import date

from model.Car import Car
from model.CarClass import CarClass
from model.Driver import Driver
from model.Engine import Engine
from model.EngineCompanies import EngineCompanies


@dataclass
class SportCar(Car):
    max_speed: decimal.Decimal
    _current_speed: decimal.Decimal
    @property
    def speed(self)->decimal.Decimal:
        return self._current_speed
    def __str__(self)->str:
        return super().__str__() \
            + f'\n max speed: {self.max_speed}' \
              f'\n current speed: {self.speed}'
#
# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# e = Engine(EngineCompanies.TOYOTA, 200)
# s = SportCar('Mers', CarClass.LORRY, decimal.Decimal(10020), d, e, 100, 99)
# c = Car('Mers', CarClass.REGULAR, decimal.Decimal(10020), d, e)
# print(s)
