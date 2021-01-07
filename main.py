from service.service import Service
from repository.repo_car_wash import RepoCarWash
from repository.filerepo_car import FileCarRepo
from tests.test_main import test_main
from console.console import Console


def main():
    car_wash_repo = RepoCarWash()
    car_repo = FileCarRepo("cars.txt")
    service = Service(car_repo, car_wash_repo)
    console = Console(service)
    console.run()


test_main()
main()
