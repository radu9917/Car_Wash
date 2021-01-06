from data_check import check_car_list
from data_check import number_check
from repository.repo_car import RepoCar
from domain.car import Car


def data_test():
    number = "AG 69 BIN"
    assert number_check(number)
    car_list = RepoCar()
    car1 = Car(1, "AG 69 BIN", "Dan")
    car2 = Car(2, "B 120 RMD", "Ion")
    car_list.store(car1)
    car_list.store(car2)
    assert not check_car_list(car_list.get_all(), "B 120 RMD")