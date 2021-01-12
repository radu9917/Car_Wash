from observer.observer_interface import Observer
from observer.observer_interface import Observable


class ObservedCar(Observable):
    def __init__(self, car):
        super().__init__()
        self.car = car

    def get_car(self):
        return self.car


class CarObserver(Observer):
    def __init__(self, observed_car, car_wash):
        self.observed_car = observed_car
        self.car_wash = car_wash

    def update(self):
        for index in self.car_wash.get_cars():
            if index == self.observed_car.get_car():
                self.car_wash.remove_car(self.observed_car.get_car())
