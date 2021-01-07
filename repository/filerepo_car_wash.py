from repository.repo_car_wash import RepoCarWash
from domain.car_wash import CarWash
from domain.car import Car


class FileCarWashRepo(RepoCarWash):
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

    def update(self, old_object, new_object):
        super().update(old_object, new_object)
        self.__store_to_file()

    def __store_to_file(self):
        file = open(self.__file_name, "w+")
        for obj in self._list:
            file.write(str(obj.get_id()) + ";" + obj.get_name() + ";")
            for car in obj.get_cars():
                file.write(str(car.get_id()) + "," + str(car.get_number()) + "," + str(car.get_owner() + ";"))
            file.write("\n")
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        lines = file.readlines()
        for line in lines:
            obj = line.split(";")
            index = obj[0]
            name = obj[1]
            car_wash = CarWash(int(index), name)
            for index2 in range(2, len(obj)):
                if obj[index2]:
                    car = obj[index2].split(",")
                    if car[0] != "\n":
                            id1 = int(car[0])
                            number = car[1]
                            name = car[2]
                            car_wash.add_car(Car(id1, number, name))
            self._list.append(car_wash)

        file.close()
