from typing import List

from model.Person import Person


class PersonRepositories:
    _persons: List[Person] = [
        Person(19, 'akjdmkjasdn'),
        Person(200, 'lkmxals')
    ]

    def add_person(self, age: int, full_name: str) -> None:
        self._persons.append(Person(age, full_name))

    def delete_person(self, full_name: str) -> None:
        person = next(p for p in self._persons if p.full_name == full_name)
        self._persons.remove(person)

    def check_existence_of_person(self, full_name: str) -> bool:
        p = next((p for p in self._persons if p.full_name == full_name), None)
        return p is not None

    @property
    def persons(self) -> List[Person]:
        return self._persons

# p = PersonRepositories()
# p.add_person(18, 'Baur')
# p.delete_person('lkmxals')
# print(p.persons)
