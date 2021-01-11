from repository.json_repo_car_wash import JsonRepoCarWash
from repository.json_repo_car import JsonRepoCar
from domain.car import Car
from domain.car_wash import CarWash


def test_json():
    car_repo = JsonRepoCar("test.json")
    car_wash_repo = JsonRepoCarWash("test.json")
    car_repo.delete(2)
    car_wash_repo.delete(2)
    car = Car(1, "AG 76 DYK", "Costi")
    car_repo.store(car)
    car_wash = CarWash(1, "Bob's")
    car_wash_repo.store(car_wash)
    assert car_wash == car_wash_repo.get(1)
    assert car == car_repo.get(1)
    car_repo.delete(1)
    car_wash_repo.delete(1)
    assert len(car_repo.get_all()) == len(car_wash_repo.get_all())
    car.set_id(2)
    car_wash.set_id(2)
    car_repo.store(car)
    car_wash_repo.store(car_wash)
