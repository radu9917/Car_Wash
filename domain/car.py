from domain.entity import Entity
from observer.observer_interface import  Observable


class Car(Entity, Observable):
    def __init__(self, index, number, owner):
        Entity.__init__(self, index)
        Observable.__init__(self)
        self.__number = number
        self.__owner = owner

    # Getters
    def get_number(self):
        return self.__number

    def get_owner(self):
        return self.__owner

    # Setters
    def set_number(self, number):
        self.__number = number

    def set_owner(self, owner):
        self.__owner = owner

    def __str__(self):
        return self.__owner + " -> " + str(self.__number)

    def __eq__(self, other):
        if self.get_id() != other.get_id():
            return False
        if self.__owner != other.get_owner():
            return False
        if self.__number != other.get_number():
            return False
        return True

    def notify(self):
        if not self.get_observers() is None:
            for car_wash in self.get_observers():
                car_wash.update(self.get_id())
