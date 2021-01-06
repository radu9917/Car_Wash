from repository.repo_car import RepoCar
from domain.car import Car


def test_car_getters():
    car = Car(1, "BOB", "Jhon")
    assert str(car.get_id()).isdecimal()
    assert car.get_owner().isalpha()
    assert car.get_number().isalpha()
    assert car.get_id() == 1
    assert car.get_number() == "BOB"
    assert car.get_owner() == "Jhon"


def test_car_setters():
    car = Car(1, "BOB", "Jhon")
    car.set_owner("IAN")
    car.set_number("NIG")
    car.set_id(2)
    assert car.get_id() == 2
    assert car.get_owner() == "IAN"
    assert car.get_number() == "NIG"
