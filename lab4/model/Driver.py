from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from model.Person import Person


class Driver(Person):
    _name: str
    _surname: str
    _started_driving_date: date

    def __init__(self, name: str, surname: str, age: int, started_driving_date: date):
        self.name = name
        self.surname = surname
        super().__init__(age=age, full_name=f'{surname} {name}')
        self._started_driving_date = started_driving_date

    def experience(self) -> str:
        delta = relativedelta(date.today(), self._started_driving_date)
        return f'years:{delta.years} month:{delta.months} days:{delta.days}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self._surname = surname

    @property
    def started_driving_date(self) -> date:
        return self._started_driving_date

    def __str__(self) -> str:
        return f'Driver({self.id=} {self.full_name=} {self.age=} {self.started_driving_date})'


# d = Driver('Baurr', 'Zh', 18, date(2000, 10, 12))
# print(d)
# print(d.experience())
