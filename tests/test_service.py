from service.service import Service
from repository.filerepo_car import FileCarRepo
from repository.filerepo_car_wash import FileCarWashRepo
from validator.validator import Validator
from domain.car import Car
from domain.car_wash import CarWash
from validator.exceptions import ValidationError


def test_functions():
    repo_car = FileCarRepo("test_car.txt")
    repo_car_wash = FileCarWashRepo("test_car_wash.txt")
    validator = Validator()
    service = Service(repo_car, repo_car_wash, validator)
    # TEST CAR FUNCTIONS
    car1 = Car(1, "AG 25 DMG", "Ian")
    service.create_car(car1)
    file = open("test_car.txt", "r")
    read_car_line = file.readline()
    file.close()
    read_car = read_car_line.split(",")
    car2 = Car(int(read_car[0]), read_car[1], read_car[2].strip("\n"))
    assert car2 == car1
    car3 = Car(1, "AG 65 DYN", "Ionel")
    service.modify_car(1, car3)
    file = open("test_car.txt", "r+")
    read_car_line = file.readline()
    read_car = read_car_line.split(",")
    car4 = Car(int(read_car[0]), read_car[1], read_car[2].strip("\n"))
    assert car4 == car3
    service.delete_car(car3.get_id())
    assert service.get_all_car() is not None
    # TEST CAR WASH FUNCTIONS
    car_wash1 = CarWash(1, "At Bob")
    service.create_car_wash(car_wash1)
    assert service.get_car_wash(1) == car_wash1
    car_wash2 = CarWash(1, "La Geani")
    service.modify_car_wash(car_wash2)
    assert service.get_car_wash(1) == car_wash2
    service.delete_car_wash(1)
    assert service.get_all_car_wash() == []
    # TEST ADD AND REMOVE FUNCTIONS
    service.create_car_wash(car_wash1)
    service.create_car(car1)
    service.add_to_car_wash(1, 1)
    car_wash2 = service.get_car_wash(1)
    assert car_wash2.get_cars() == [car1]
    service.remove_from_car_wash(1, 1)
    car_wash2 = service.get_car_wash(1)
    assert car_wash2.get_cars() == []
    file2 = open("test_car_wash.txt", "w")
    file.truncate(0)
    file2.truncate(0)
    file.close()
    try:
        service.test_input("2", 12)
        assert True
    except ValidationError:
        assert False
