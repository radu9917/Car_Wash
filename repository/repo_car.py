from repository.repo_interface import RepoInterface


class RepoCar(RepoInterface):
    def __init__(self):
        self._list = []

    def get_all(self):
        return self._list

    def store(self, obj):
        self._list.append(obj)

    def get(self, obj_id):
        for car in self._list:
            if car.get_id() == obj_id:
                return car

    def update(self, old_object, new_object):
        for car in self._list:
            if car.get_id() == old_object:
                car.set_id(new_object.get_id())
                car.set_owner(new_object.get_owner())
                car.set_number(new_object.get_number())

    def delete(self, obj_id):
        for car in self._list:
            if car.get_id() == obj_id:
                self._list.remove(car)
