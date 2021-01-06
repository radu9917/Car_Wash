from repository.repo_interface import RepoInterface


class RepoCar(RepoInterface):
    def __init__(self):
        self.__list = []

    def get_all(self):
        return self.__list

    def store(self, obj):
        self.__list.append(obj)

    def get(self, obj_id):
        for car in self.__list:
            if car.get_id() == obj_id:
                return car

    def update(self, old_object, new_object):
        for car in self.__list:
            if car.get_id() == old_object:
                car.set_owner(new_object.get_owner())
                car.set_number(new_object.get_number())

    def delete(self, obj_id):
        for car in self.__list:
            if car.get_id() == obj_id:
                self.__list.remove(car)
