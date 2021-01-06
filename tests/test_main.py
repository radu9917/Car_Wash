from tests.test_car import test_car_getters
from tests.test_car import test_car_setters
from tests.test_car_wash import test_car_wash_getters
from tests.test_car_wash import test_car_wash_setters
from tests.test_car_repo import car_repo_test
from tests.test_car_wash_repo import test_car_wash_repo
from tests.test_data_check import data_test


def test_main():
    # TEST CAR
    test_car_getters()
    test_car_setters()
    # TEST CAR WASH
    test_car_wash_getters()
    test_car_setters()
    # TEST CAR REPO
    car_repo_test()
    # TEST CAR WASH REPO
    test_car_wash_repo()
    # TEST DATA CHECK
    data_test()

