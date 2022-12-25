import uuid
from abc import ABC

class Person(ABC):
    _id: uuid
    _age: int
    _full_name: str

    def __init__(self, age: int, full_name: str):
        self.id = uuid.uuid4()
        self.age = age
        self.full_name = full_name

    @property
    def id(self) -> uuid:
        return self._id

    @id.setter
    def id(self, person_id: uuid) -> None:
        self._id = person_id

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str) -> None:
        self._full_name = full_name

    def __str__(self) -> str:
        return f'Person( {self.id=} {self.full_name=} {self.age=})\n'

# p = Person(19, 'akjdmkjasdn')
# print(p)
