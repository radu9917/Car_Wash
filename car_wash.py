
class CarWash:
    def __init__(self, index, name, cars):
        self.id = index
        self.name = name
        self.cars = cars

    def adding_car(self):
        self.cars += 1

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
