import uuid

from model.EngineCompanies import EngineCompanies


class Engine:
    company: EngineCompanies
    power: int

    def __init__(self, company: EngineCompanies, power: int):
        self.id = uuid.uuid4()
        self.company = company
        self.power = power

    def __repr__(self) -> str:
        return f'Engine(id: {self.id} company: {self.company} power: {self.power}'

# e = Engine(EngineCompanies.TOYOTA,200)
# print(e)