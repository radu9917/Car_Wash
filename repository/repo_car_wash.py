from repository.repo_interface import RepoInterface


class RepoCarWash(RepoInterface):
    def __init__(self):
        self._list = []

    def get_all(self):
        return self._list

    def store(self, obj):
        self._list.append(obj)

    def get(self, obj_id):
        for car_wash in self._list:
            if car_wash.get_id() == obj_id:
                return car_wash

    def update(self, new_object):
        for car_wash in self._list:
            if car_wash.get_id() == new_object.get_id():
                car_wash.set_id(new_object.get_id())
                car_wash.set_name(new_object.get_name())
                car_wash.set_cars(new_object.get_cars())

    def delete(self, obj_id):
        for car_wash in self._list:
            if car_wash.get_id() == obj_id:
                self._list.remove(car_wash)
