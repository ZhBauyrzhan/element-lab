from dataclasses import dataclass

from model.Car import Car


@dataclass
class SportCar(Car):
    max_speed: int

    def speed(self) -> int:
        return self.max_speed

    def __repr__(self) -> str:
        return super().__str__() \
            + f'\n max speed: {self.max_speed}' \
              f'\n current speed: {self.speed}'
#
# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# e = Engine(EngineCompanies.TOYOTA, 200)
# s = SportCar('Mers', CarClass.LORRY, decimal.Decimal(10020), d, e, 100, 99)
# c = Car('Mers', CarClass.REGULAR, decimal.Decimal(10020), d, e)
# print(s)
