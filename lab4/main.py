import sys
from datetime import datetime

from handlers.CarHandler import CarHandler
from handlers.DriverHandler import DriverHandler
from handlers.PersonHandler import PersonHandler
from model.CarClass import CarClass
from model.Engine import Engine
from model.EngineCompanies import EngineCompanies
from repositories.CarRepositories import CarRepositories
from repositories.DriverRepositories import DriverRepositories
from repositories.PersonRepositories import PersonRepositories
from services.CarService import CarService
from services.DriverService import DriverService
from services.PersonService import PersonService


def init():
    person_repository = PersonRepositories()
    person_service = PersonService(person_repository)
    person_handler = PersonHandler(person_service)

    driver_repository = DriverRepositories()
    driver_service = DriverService(driver_repository)
    driver_handler = DriverHandler(driver_service)

    car_repository = CarRepositories()
    car_service = CarService(car_repository)
    car_handler = CarHandler(car_service)
    while True:
        print('Choose action:')
        print('1. Create person account')
        print('2. Delete person by full name')
        print('3. Print all existed persons')
        print('4. Create driver')
        print('5. Delete driver by full name')
        print('6. Print all existed drivers')
        print('7. Create car')
        print('8. Delete car by uuid(uuid4)')
        print('9. Print all existed cars')
        print('Q. quit')
        command = input()
        match command:
            case 'Q':
                sys.exit(0)
            case '1':
                age = int(input('Input age: '))
                full_name = input('Input full name: ')
                print(person_handler.create_person(age, full_name))
            case '2':
                full_name = input('Input full name: ')
                print(person_handler.delete_person(full_name))
            case '3':
                people = person_handler.get_people()
                for i in people:
                    print(i)
            case '4':
                name = input('Input name')
                surname = input('Input surname')
                age = int(input('Input age: '))
                started_driving_date = datetime.strptime(input('Input started driving date :'), '%m-%d-%Y').date()
                print(driver_handler.create_drive(name, surname, age, started_driving_date))
            case '5':
                full_name = input('Input full name: ')
                print(driver_handler.delete_drive(full_name))
            case '6':
                drivers = driver_handler.get_driver()
                for i in drivers:
                    print(i)
            case '7':
                car_class = input('Input car class')
                car_brand = input('Input car brand')
                car_class = CarClass.SPORT_CAR
                weight = int(input('Input car brand'))
                driver_name = input('Input drive name')
                driver = driver_handler.get_driver_by_full_name(driver_name)
                if driver is None:
                    print('No such driver')
                    continue
                engine_company = input('Input engine monufacture company name')
                engine_company = next((e for e in EngineCompanies if e.value == engine_company), None)
                engine_power = int(input('Input engine Power'))
                engine = Engine(engine_company, engine_power)
                if engine is None:
                    print('No such engine monufacture company')
                    continue
                match car_class:
                    case 'sport':
                        max_speed = int(input('Input max speed'))
                        car_handler.create_car(
                            car_brand=car_brand,
                            car_class=CarClass.SPORT_CAR,
                            weight=weight,
                            driver=driver,
                            engine=engine,
                            max_speed=max_speed
                        )
                    case 'lorry':
                        max_people = int(input('Input max speed'))
                        car_handler.create_car(
                            car_brand=car_brand,
                            car_class=CarClass.LORRY,
                            weight=weight,
                            driver=driver,
                            engine=engine,
                            max_people_amount=max_people
                        )
                    case 'regular':
                        car_handler.create_car(
                            car_brand=car_brand,
                            car_class=CarClass.LORRY,
                            weight=weight,
                            driver=driver,
                            engine=engine,
                        )
if __name__ == "__main__":
    init()
