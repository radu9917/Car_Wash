
class CarWash:
    def __init__(self, index, name):
        self.id = index
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cars(self):
        return self.cars

    # Setters
    def set_id(self, index):
        self.id = index

    def set_name(self, name):
        self.name = name

    def set_cars(self, cars):
        self.cars = cars

    def __str__(self):
        cars = ""
        for car in self.get_cars():
            cars += str(car)
        return self.get_name() + " with " + cars + " queued\n"
