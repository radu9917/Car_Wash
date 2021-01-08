from repository.repo_car import RepoCar
from domain.car import Car


def car_repo_test():
    car_list = RepoCar()
    car1 = Car(1, "AG 46 IMD", "Ion")
    car_list.store(car1)
    assert car_list.get_all() is not None
    car2 = Car(2, "B 314 ZDA", "Miron")
    car_list.update(1, car2)
    assert car_list.get_all()[0] == car2
    car_list.store(car1)
    car_list.delete(2)
    assert car_list.get_all() == [car1]
    assert car_list.get(2) == car1
