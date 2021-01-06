from domain.car_wash import CarWash
from domain.car import Car


def test_car_wash_getters():
    car_wash = CarWash(1, "BOB")
    car = Car(1, "IAN", "ION")
    car_wash.add_car(car)

    assert car_wash.get_id() == 1
    assert car_wash.get_name() == "BOB"
    assert car_wash.get_cars() == [car]


def test_car_wash_setters():
    car_wash = CarWash(1, "BOB")
    car_wash.set_id(2)
    car_wash.set_name("IAN")
    assert car_wash.get_id() == 2
    assert car_wash.get_name() == "IAN"

