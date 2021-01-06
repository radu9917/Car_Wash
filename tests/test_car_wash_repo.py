from repository.repo_car_wash import RepoCarWash
from domain.car_wash import CarWash


def test_car_wash_repo():
    car_wash_list = RepoCarWash()
    car_wash = CarWash(1, "Bob")
    car_wash_list.store(car_wash)
    assert car_wash_list.get_all() is not None
    car_wash2 = CarWash(1, "Ian")
    car_wash_list.update(1,car_wash2)
    assert car_wash_list.get_all()[0] == car_wash2
    car_wash_list.delete(1)
    car_wash_list.store(car_wash)
    assert car_wash_list.get_all() is not None
