from service.service import Service
from repository.filerepo_car import FileCarRepo
from repository.filerepo_car_wash import FileCarWashRepo
from validator.validator import Validator
from domain.car import Car

def test_functions():
    repo_car = FileCarRepo("test.txt")
    repo_car_wash = FileCarWashRepo("test.txt")
    validator = Validator()
    service = Service(repo_car, repo_car_wash , validator)
    # TEST CAR FUNCTIONS
    car1 = Car(1, "AG 25 DMG", "Ian")
    service.create_car(car1)
    file = open("test.txt")
    read_car = file.readline()
    car2 = Car(int(read_car[0]), read_car[1], read_car[2].strip("\n"))
    assert car2 == car1
    car3 = Car(1, "AG 65 DYN", "Ionel")
    service.modify_car(1, car3)
    read_car = file.readline()
    car4 = Car(int(read_car[0]), read_car[1], read_car[2].strip("\n"))
    assert car4 == car3
    service.delete_car(car3.get_id())
    assert service.get_all_car() is None






