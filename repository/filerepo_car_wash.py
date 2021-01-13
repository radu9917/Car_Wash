from repository.repo_car_wash import RepoCarWash
from domain.car_wash import CarWash


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

    def modify(self, new_object):
        super().modify(new_object)
        self.__store_to_file()

    def __store_to_file(self):
        file = open(self.__file_name, "w+")
        for obj in self._list:
            file.write(str(obj.get_id()) + ";" + obj.get_name())
            car_list = obj.get_cars()
            car_list_len = len(car_list)
            if car_list_len > 0:
                file.write(";")
            for index in range(car_list_len):
                file.write(str(car_list[index]))
                if index != car_list_len - 1:
                    file.write(",")
            file.write("\n")
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        lines = file.readlines()

        for line in lines:
            line.rstrip()
            obj = line.split(";")
            index = obj[0]
            name = obj[1]
            car_wash = CarWash(int(index), name)
            if len(obj) >= 3:
                car_list = obj[2].split(",")
                if car_list:
                    for car in car_list:
                        car_wash.add_car(int(car))
                self._list.append(car_wash)

        file.close()
