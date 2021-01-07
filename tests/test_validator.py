from validator.validator import Validator
from domain.car import Car
from domain.car_wash import CarWash
from repository.repo_car import RepoCar


def test_validation():
    validator = Validator()
    car = Car(1, "AG 12 BOB", "Dan")
    validator.validate_car(car)
    car_wash = CarWash(1, "La Ionel")
    validator.validate_car_wash(car_wash)
    car_list = RepoCar()
    car_list.store(car)
    validator.id_find(car_list, int(car.get_id()))
    car2 = Car(2, "AG 67 IAD", "Iulian")
    validator.id_check(car_list, int(car2.get_id()))
    validator.option_check("2", 8)
