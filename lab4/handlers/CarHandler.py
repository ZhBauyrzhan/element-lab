import uuid
from typing import List

from exceptions.CarAlreadyExistsError import CarAlreadyExistsError
from exceptions.NoSuchCarError import NoSuchCarError
from model.Car import Car
from model.CarClass import CarClass
from model.Lorry import Lorry
from model.SportCar import SportCar
from services.CarService import CarService


class CarHandler:
    def __init__(self, service: CarService):
        self._service = service

    def create_car(self, **kwargs) -> str:
        try:
            match kwargs.car_class:
                case CarClass.SPORT_CAR:
                    self._service.create_car(SportCar(
                        kwargs.car_brand,
                        kwargs.car_class,
                        kwargs.weight,
                        kwargs.driver,
                        kwargs.engine,
                        kwargs.max_speed,
                    ))
                case CarClass.LORRY:
                    self._service.create_car(Lorry(
                        kwargs.car_brand,
                        kwargs.car_class,
                        kwargs.weight,
                        kwargs.driver,
                        kwargs.engine,
                        kwargs.max_people_amount,
                    ))
                case CarClass.REGULAR:
                    self._service.create_car(Car(
                        kwargs.car_brand,
                        kwargs.car_class,
                        kwargs.weight,
                        kwargs.driver,
                        kwargs.engine,
                    ))
            return f'Successfully created car'
        except CarAlreadyExistsError:
            return f'Car already exists error'

    def delete_car(self, search_id: uuid) -> str:
        try:
            self._service.delete_car(search_id)
            return f'Car was successfully deleted'
        except NoSuchCarError:
            return f'No such car error'

    def get_cars(self) -> List[Car]:
        return self._service.get_cars()