from repository.repo_interface import RepoInterface


class RepoCarWash(RepoInterface):
    def __init__(self):
        self.__list = []

    def get_all(self):
        return self.__list

    def store(self, obj):
        self.__list.append(obj)

    def get(self, obj_id):
        for car_wash in self.__list:
            if car_wash.get_id() == obj_id:
                return car_wash

    def update(self, old_object, new_object):
        for car_wash in self.__list:
            if car_wash == old_object:
                car_wash.set_id(new_object.get_id())
                car_wash.set_name(new_object.get_name())
                car_wash.set_cars(new_object.get_cars())

    def delete(self, obj_id):
        for car_wash in self.__list:
            if car_wash.get_id() == obj_id:
                self.__list.remove(car_wash)
