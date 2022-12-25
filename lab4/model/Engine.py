import uuid

from model.EngineCompanies import EngineCompanies


class Engine:
    id: uuid
    _company: EngineCompanies
    _horse_power: int

    def __init__(self, company: EngineCompanies, power: int):
        self.id = uuid.uuid4()
        self._company = company
        self._horse_power = power

    @property
    def power(self) -> int:
        return self._horse_power

    @property
    def company(self) -> EngineCompanies:
        return self._company

    def __str__(self) -> str:
        return f'Engine(id: {self.id} company: {self._company} power: {self.power}'


# @dataclass
#
# e = Engine(EngineCompanies.TOYOTA,200)
# print(e)
