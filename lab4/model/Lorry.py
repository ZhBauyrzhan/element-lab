import decimal
from dataclasses import dataclass
from datetime import date

from model.Car import Car
from model.CarClass import CarClass
from model.Driver import Driver
from model.Engine import Engine
from model.EngineCompanies import EngineCompanies


@dataclass
class Lorry(Car):
    max_people_amount: int
    _carrying: int

    @property
    def carrying(self) -> int:
        return self._carrying

    def __repr__(self) -> str:
        return super().__str__() \
            + f'\n max people amount: {self.max_people_amount}' \
            f'\n carrying people amount: {self.carrying}'


#
# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# e = Engine(EngineCompanies.TOYOTA, 200)
# l = Lorry('Mers', CarClass.LORRY, decimal.Decimal(10020), d, e, 10, 1)
# c = Car('Mers', CarClass.REGULAR, decimal.Decimal(10020), d, e)
# print(l)
