from domain.car_wash import CarWash
from domain.car import Car


def test_car_wash_getters():
    car_wash = CarWash(1, "BOB")
    car = Car(1, "IAN", "ION")
    car_wash.add_car(car.get_id())

    assert car_wash.get_id() == 1
    assert car_wash.get_name() == "BOB"
    assert car_wash.get_cars() == [car.get_id()]


def test_car_wash_setters():
    car_wash = CarWash(1, "BOB")
    car_wash.set_id(2)
    car_wash.set_name("IAN")
    assert car_wash.get_id() == 2
    assert car_wash.get_name() == "IAN"


def test_car_wash_str():
    car_wash1 = CarWash(1, "Bob")
    car_wash2 = CarWash(1, "Bob")
    car1 = Car(1, "AG 67 NIG", "Ion")
    car_wash1.add_car(car1.get_id())
    car_wash2.add_car(car1.get_id())
    assert str(car_wash1) == str(car_wash2)


def test_car_wash_eq():
    car_wash1 = CarWash(1, "Bob")
    car_wash2 = CarWash(1, "Bobul")
    car_wash3 = CarWash(1, "Bob")
    car_wash4 = CarWash(2, "Bob")
    car1 = Car(1, "AG 67 NIG", "Ion")
    car_wash3.add_car(car1.get_id())
    assert not car_wash1 == car_wash2
    assert not car_wash1 == car_wash3
    assert not car_wash1 == car_wash4


def test_car_wash():
    test_car_wash_eq()
    test_car_wash_str()
    test_car_wash_getters()
    test_car_wash_setters()