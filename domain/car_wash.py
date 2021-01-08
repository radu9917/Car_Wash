from domain.entity import Entity


class CarWash(Entity):
    def __init__(self, index, name):
        super().__init__(index)
        self.__name = name
        self.__cars = []

    def add_car(self, car):
        int(car)
        self.__cars.append(car)

    def remove_car(self, car):
        int(car)
        self.__cars.remove(car)

    # Getters
    def get_name(self):
        return self.__name

    def get_cars(self):
        return self.__cars

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_cars(self, cars):
        self.__cars = cars

    def __str__(self):
        cars = ""
        nr = 0
        for car in self.get_cars():
            nr += 1
        return self.get_name() + " with " + str(nr) + " cars queued\n"

    def __eq__(self, other):
        if self.__name != other.get_name():
            return False
        if self.__id != int(other.get_id()):
            return False
        if self.__cars != other.get_cars():
            return False
        return True
