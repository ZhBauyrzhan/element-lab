from typing import List

from exceptions.NoSuchPersonError import NoSuchPersonError
from exceptions.PersonAlreadyExistsError import PersonAlreadyExistsError
from model.Person import Person
from repositories.PersonRepositories import PersonRepositories


class PersonService:
    _repository: PersonRepositories

    def __init__(self, repository: PersonRepositories):
        self._repository = repository

    def create_person(self, person: Person) -> None:
        if not self._repository.check_existence_of_person(person.full_name):
            self._repository.add_person(person)
        else:
            raise PersonAlreadyExistsError

    def delete_person(self, full_name: str) -> None:
        if self._repository.check_existence_of_person(full_name):
            self._repository.delete_person(full_name)
        else:
            raise NoSuchPersonError

    def get_people(self) -> List[Person]:
        return self._repository.people
