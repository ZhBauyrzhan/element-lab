import uuid
from abc import ABC


class Person(ABC):
    _id: uuid
    age: int
    full_name: str

    def __init__(self, age: int, full_name: str):
        self._id = uuid.uuid4()
        self.age = age
        self.full_name = full_name

    @property
    def id(self) -> uuid:
        return self._id

    def __repr__(self) -> str:
        return f'Person( {self.id=} {self.full_name=} {self.age=})'

# p = Person(19, 'akjdmkjasdn')
# print(p)
