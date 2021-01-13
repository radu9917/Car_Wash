from repository.json_repo_car_wash import JsonRepoCarWash
from repository.json_repo_car import JsonRepoCar
from domain.car import Car
from domain.car_wash import CarWash
import json


def test_json():
    car_repo = JsonRepoCar("test.json")
    car_wash_repo = JsonRepoCarWash("test.json")
    car_repo.delete(1)
    car_wash_repo.delete(1)
    car = Car(1, "AG 76 DYK", "Costi")
    car_repo.store(car)
    car_wash = CarWash(1, "Bob's")
    car_wash_repo.store(car_wash)
    assert car_wash == car_wash_repo.get(1)
    assert car == car_repo.get(1)
    assert len(car_repo.get_all()) == len(car_wash_repo.get_all())
    car_repo.modify(1, Car(1, "AG 69 COC", "Sorin"))
    car_wash_repo.modify(CarWash(1, "La Daniel"))
    car_r2 = JsonRepoCar("test_else.json")
    car_r2.store(car)
    car_w_r2 = JsonRepoCarWash("test_else2.json")
    car_w_r2.store(car_wash)
    car_r2.delete(1)
    car_w_r2.delete(1)

