from tests.test_car import test_car
from tests.test_car_wash import test_car_wash
from tests.test_car_repo import car_repo_test
from tests.test_car_wash_repo import test_car_wash_repo
from tests.test_validator import test_validation
from tests.test_service import test_functions
from tests.test_filerepo import test_load


def test_main():
    # TEST CAR
    test_car()
    # TEST CAR WASH
    test_car_wash()
    # TEST CAR REPO
    car_repo_test()
    # TEST CAR WASH REPO
    test_car_wash_repo()
    # TEST VALIDATION
    test_validation()
    # TEST SERVICE
    test_functions()
    # TEST FILE LOAD
    test_load()

