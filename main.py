from service.service import Service
from repository.filerepo_car_wash import FileCarWashRepo
from repository.filerepo_car import FileCarRepo
from tests.test_main import test_main
from console.console import Console


def main():
    car_wash_repo = FileCarWashRepo("car_wash.txt")
    car_repo = FileCarRepo("cars.txt")
    service = Service(car_repo, car_wash_repo)
    console = Console(service)
    console.run()


test_main()
main()
