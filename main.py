from service.service import Service
from tests.test_main import test_main
from console.console import Console
from validator.validator import Validator
from repository.json_repo_car import JsonRepoCar
from repository.json_repo_car_wash import JsonRepoCarWash



def main():
    car_wash_repo = JsonRepoCarWash("car_wash.json")
    car_repo = JsonRepoCar("car_wash.json")
    validator = Validator()
    service = Service(car_repo, car_wash_repo, validator)
    console = Console(service)
    console.run()


test_main()
main()


