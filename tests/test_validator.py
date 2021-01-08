from validator.validator import Validator
from domain.car import Car
from domain.car_wash import CarWash
from repository.repo_car import RepoCar
from validator.exceptions import ValidationError

def test_validation():
    validator = Validator()
    car1 = Car(1, "ag 12 BOB", "Dan")
    car3 = Car(":", "A", "Ian")
    car4 = Car(4, "A", "Ian")
    car5 = Car(2, "12 12 BAG", "Dan")
    car6 = Car(2, "AG ASD BUD", "Dan")
    car7 = Car(2, "AG 12 IMD", "dan")
    car8 = Car(2, "AG 12 IMD", "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    car9 = Car(2, "AG 12 1234", "Ion")
    try:
        validator.validate_car(car1)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car4)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car3)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car5)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car6)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car7)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car8)
        assert False
    except ValidationError:
        assert True
    try:
        validator.validate_car(car9)
        assert False
    except ValidationError:
        assert True

    car_wash1 = CarWash(1, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    car_wash2 = CarWash(";", "La Geani")

    try:
        validator.validate_car_wash(car_wash1)
        assert False
    except ValidationError:
        assert True

    try:
        validator.validate_car_wash(car_wash2)
        assert False
    except ValidationError:
        assert True
    car_list = RepoCar()
    car_list.store(car1)

    try:
        validator.id_find(car_list, 6)
        assert False
    except ValidationError:
        assert True

    car2 = Car(2, "AG 67 :AD", "Iulian")
    car_list.store(car2)

    try:
        validator.id_check(car_list, 2)
        assert False
    except ValidationError:
        assert True

    try:
        validator.option_check("8", 2)
        assert False
    except ValidationError:
        assert True
