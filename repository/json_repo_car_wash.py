from repository.repo_car_wash import RepoCarWash
from domain.car_wash import CarWash
import json


class JsonRepoCarWash(RepoCarWash):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def store(self, obj):
        super().store(obj)
        self.__store_to_file()

    def delete(self, obj_id):
        super().delete(obj_id)
        self.__store_to_file()

    def update(self, new_object):
        super().update(new_object)
        self.__store_to_file()

    def __store_to_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        car_washes = []

        for obj in self._list:
            id_car_wash = obj.get_id()
            name = obj.get_name()
            cars = obj.get_cars()
            car_wash = {
                "id": id_car_wash,
                "name": name,
                "cars": cars
            }
            car_washes.append(car_wash)
        if "car" in json_file:
            car = json_file["car"]
            clist = {
                "car": car,
                "car_wash": car_washes
            }
        else:
            clist = {
                "car_wash": car_washes
            }
        string1 = json.dumps(clist, indent=4)
        file.close()
        file = open(self.__file_name, "w")
        file.write(string1)
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r+")
        json_file = json.loads(file.read())
        if "car_wash" in json_file:
            for index in json_file["car_wash"]:
                id_car_wash = index["id"]
                name = index["name"]
                cars = index["cars"]
                car_wash = CarWash(id_car_wash, name)
                car_wash.set_cars(cars)
                self._list.append(car_wash)
        file.close()
