from domain.car import Car
from domain.car_wash import CarWash
from service.service import Service
from repository.repo_car_wash import RepoCarWash
from repository.repo_car import RepoCar


def test_observer():
    car_list = RepoCar()
    car_wash_list = RepoCarWash()
    car = Car(1, "AG 67 NIG", "Radu")
    car_wash = CarWash(1, "Geani's")
    car.add_observer(car_wash)
    car_list.store(car)
    assert len(car_list.get_all()) == 1
    car_wash_list.store(car_wash)
    car_wash_list.get(1).add_car(car.get_id())
    assert len(car_wash_list.get(1).get_cars()) == 1
    car_list.delete(car.get_id())
    assert len(car_list.get_all()) == 0
    assert len(car_wash_list.get(1).get_cars()) == 0


