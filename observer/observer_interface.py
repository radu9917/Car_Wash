class Observable:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        pass

    def get_observers(self):
        return self.__observers


class Observer:
    def update(self):
        pass
