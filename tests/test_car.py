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


def test_car_str():
    car1 = Car(1, "AG 67 BUN", "Dan")
    car2 = Car(1, "AG 67 BUN", "Dan")
    assert str(car1) == str(car2)


def test_car_eq():
    car1 = Car(1, "AG 67 BUN", "Dan")
    car2 = Car(2, "AG 67 BUN", "Dan")
    car3 = Car(1, "AG 77 BUN", "Dan")
    car4 = Car(1, "AG 67 BUN", "Ian")
    assert not car1 == car2
    assert not car1 == car3
    assert not car1 == car4


def test_car():
    test_car_str()
    test_car_eq()
    test_car_setters()
    test_car_getters()