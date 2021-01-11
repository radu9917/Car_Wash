from repository.repo_car import RepoCar
from repository.repo_car_wash import RepoCarWash
from repository.filerepo_car import FileCarRepo
from repository.filerepo_car_wash import FileCarWashRepo
from repository.json_repo_car import JsonRepoCar
from repository.json_repo_car_wash import JsonRepoCarWash

class Factory:
    __instance = None
    @staticmethod
    def get_instance():
        if not Factory.__instance:
            Factory()
        return Factory.__instance

    def __init__(self):
        if Factory.__instance:
            raise Exception("Instance already created")
        Factory.__instance = self

    def create_car_repo(self, backend, file_name):
        method = {
            "memory": RepoCar,
            "csv": FileCarRepo,
            "json": JsonRepoCar
        }
        if backend == "memory":
            return method[backend]()
        return method[backend](file_name)

    def create_car_wash_repo(self, backend, file_name):
        method = {
            "memory": RepoCarWash,
            "csv": FileCarWashRepo,
            "json": JsonRepoCarWash
        }
        if backend == "memory":
            return method[backend]()
        return method[backend](file_name)
