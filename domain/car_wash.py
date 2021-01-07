
class CarWash:
    def __init__(self, index, name):
        self.__id = index
        self.__name = name
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)

    def remove_car(self, car):
        self.__cars.remove(car)

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cars(self):
        return self.__cars

    # Setters
    def set_id(self, index):
        self.__id = index

    def set_name(self, name):
        self.__name = name

    def set_cars(self, cars):
        self.__cars = cars

    def __str__(self):
        cars = ""
        for car in self.get_cars():
            cars += str(car)
        return self.get_name() + " with " + cars + " queued\n"

    def __eq__(self, other):
        if self.__name != other.get_name():
            return False
        if self.__id != int(other.get_id()):
            return False
        if self.__cars != other.get_cars():
            return False
        return True
