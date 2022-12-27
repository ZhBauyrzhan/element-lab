from typing import List

from exceptions.NoSuchPersonError import NoSuchPersonError
from exceptions.PersonAlreadyExistsError import PersonAlreadyExistsError
from model.Person import Person
from services.PersonService import PersonService


class PersonHandler:
    def __init__(self, service: PersonService):
        self._service = service

    def create_person(self, age: int, full_name: str) -> str:
        try:
            self._service.create_person(Person(age, full_name))
            return f'Successfully created person'
        except PersonAlreadyExistsError:
            return f'Person already exists'

    def delete_person(self, full_name: str) -> str:
        try:
            self._service.delete_person(full_name)
            return 'Successfully deleted person'
        except NoSuchPersonError:
            return 'No such person error'

    def get_people(self) -> List[Person]:
        return self._service.get_people()
