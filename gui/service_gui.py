# This Python file uses the following encoding: utf-8
from service.service import Service
from PySide2.QtCore import QObject, Slot, Signal, Property
from domain.car import Car


class ServiceGUI(Service, QObject):
    def __init__(self):
        QObject.__init__()

    @Slot(str, str)
    def create_car(self, car_owner, car_number):
        car = Car(owner=car_owner, number=car_number)
        Service.create_car(car)

    @Slot(int)
    def delete_car(self, car_id):
        Service.delete_car(car_id)

    @Slot(str, str, int)
    def update_car(self, car_owner, car_number, car_id):
        new_car = Car(owner=car_owner, number=car_number)
        Service.modify_car(car_id, new_car)

    @Property(list)
    def get_all_car(self):
        pass
