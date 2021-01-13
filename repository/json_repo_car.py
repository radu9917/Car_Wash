from repository.repo_car import RepoCar
from domain.car import Car
import json


class JsonRepoCar(RepoCar):
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

    def modify(self, old_object, new_object):
        super().modify(old_object, new_object)
        self.__store_to_file()

    def __store_to_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        car = []
        for obj in self._list:
            id_car = obj.get_id()
            number = obj.get_number()
            owner = obj.get_owner()
            car_ob = {
                "id": id_car,
                "number": number,
                "owner": owner
            }

            car.append(car_ob)
        if "car_wash" in json_file:
            car_washes = json_file["car_wash"]
            clist = {
                "car": car,
                "car_wash": car_washes
            }
        else:
            clist = {
                "car": car
            }
        file.close()
        file = open(self.__file_name, "w")
        string2 = json.dumps(clist, indent=4)
        file.write(string2)
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        if "car" in json_file:
            for index in json_file["car"]:
                id_car = index["id"]
                number = index["number"]
                name = index["owner"]
                self._list.append(Car(id_car, number, name))
        file.close()
