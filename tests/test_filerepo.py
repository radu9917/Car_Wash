from repository.filerepo_car import FileCarRepo
from repository.filerepo_car_wash import FileCarWashRepo
from domain.car import Car
from domain.car_wash import CarWash


def test_load():
    car_repo = FileCarRepo("test_car.txt")
    car_wash_repo = FileCarWashRepo("test_car_wash.txt")
    car = Car(1, "AG 67 DYC", "Radu")
    car_wash = CarWash(1, "La Bob")
    car_repo.store(car)
    car_wash.add_car(car)
    car_wash_repo.store(car_wash)
    test_car_repo = FileCarRepo("test_car.txt")
    test_car_wash_repo = FileCarWashRepo("test_car_wash.txt")
    assert test_car_repo.get(1) == car
    assert test_car_wash_repo.get(1) == car_wash
    file1 = open("test_car.txt", "w")
    file2 = open("test_car_wash.txt", "w")
    file1.truncate(0)
    file2.truncate(0)
    file1.close()
    file2.close()

