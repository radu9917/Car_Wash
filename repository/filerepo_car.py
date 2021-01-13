from repository.repo_car import RepoCar
from domain.car import Car


class FileCarRepo(RepoCar):
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
        file = open(self.__file_name, "w")
        for obj in self._list:
            file.write(str(obj.get_id()) + "," + obj.get_number() + "," + obj.get_owner() + "\n")
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        lines = file.readlines()
        for line in lines:
            obj = line.split(",")
            index = int(obj[0])
            number = obj[1]
            name = obj[2].strip("\n")
            self._list.append(Car(index, number, name))

        file.close()
