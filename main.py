from service.service import Service
from tests.test_main import test_main
from console.console import Console
from validator.validator import Validator
from factory.factory import Factory


def main():
    factory = Factory.get_instance()
    car_wash_repo = factory.create_car_wash_repo("json", "car_wash.json")
    car_repo = factory.create_car_repo("json", "car_wash.json")
    validator = Validator()
    service = Service(car_repo, car_wash_repo, validator)
    console = Console(service)
    console.run()


test_main()
main()



