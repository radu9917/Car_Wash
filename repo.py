# CRUD - CREATE READ UPDATE DELETE
class Repo:
    def __init__(self):
        self.__list = []

    def find_all(self):
        return self.__list

    def store(self, obj):
        self.__list.append(obj)

    def get(self, id):
        for ob in self.__list:
            if ob.get_id() == id:
                return ob

    def update(self, id, obj):
        for ob in self.__list:
            if ob.get_id() == id:
                ob.set_owner(obj.get_owner())
                ob.set_number(obj.get_number())

    def delete(self, id):
        for ob in self.__list:
            if ob.get_id() == id:
                self.__list.remove(ob)
                return ob
