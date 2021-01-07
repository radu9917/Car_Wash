from domain.car_wash import CarWash
from domain.car import Car
from validator.exceptions import ValidationError
from console.colors import font_colors


class Console:
    def __init__(self, service):
        self.__service = service

    def create_car(self):
        nr = int(input("How many cars do you want to make?"))
        while nr > 0:
            print("Create car :")
            index = input("Give car index:")
            number = input("Give car number:")
            owner = input("Give car owner:")
            try:
                self.__service.create_car(Car(index, number, owner))
                nr -= 1
                print(font_colors.OKGREEN + "Car successfully added" + font_colors.ENDC)
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def create_car_wash(self):
        nr = int(input("How many car washes do you wan to create"))
        while nr > 0:
            print("Create car wash:")
            index = int(input("Give index:"))
            name = input("Give name:")
            try:
                self.__service.create_car_wash(CarWash(index, name))
                nr -= 1
                print(font_colors.OKGREEN + "Car successfully added" + font_colors.ENDC)
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def delete_car_wash(self):
        index = int(input("Choose a car wash to delete"))
        try:
            self.__service.delete_car_wash(index)
            print(font_colors.OKGREEN + "Car wash successfully deleted" + font_colors.ENDC)
        except ValidationError as exp:
            print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def show_cars(self):
        for car in self.__service.get_all_car():
            print(car)

    def delete_car(self):
        index = int(input("What car do you want to delete?"))
        try:
            self.__service.delete_car(index)
            print(font_colors.OKGREEN + "Car successfully deleted" + font_colors.ENDC)
        except ValidationError as exp:
            print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def modify_car(self):
        correct = False

        while not correct:
            index = int(input("What car do you want to change?"))
            number = input("Give car number")
            owner = input("Give car owner")
            car = Car(index, number, owner)
            try:
                self.__service.modify_car(index, car)
                print(font_colors.OKGREEN + "Car successfully modified" + font_colors.ENDC)
                correct = True
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def view_all_car_wash(self):
        for car_wash in self.__service.get_all_car_wash():
            print(car_wash)

    def view_car_wash(self):
        choice = int(input("Choose a car wash"))
        correct = False
        while not correct:
            try:
                print(self.__service.get_car_wash(choice))
                correct = True
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def modify_car_wash(self):
        correct = False
        while not correct:
            j = int(input("Choose a car wash to rename:"))
            name = input("Choose the name for the car wash")
            car_wash = CarWash(j, name)
            try:
                self.__service.modify_car_wash(car_wash)
                correct = True
                print(font_colors.OKGREEN + "Car wash successfully modified" + font_colors.ENDC)
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def add_to_car_wash(self):

        correct = False
        while not correct:
            try:
                choice1 = int(input("Choose a car wash"))
                choice2 = int(input("Choose the car you want to be added"))
                self.__service.add_to_car_wash(choice1, choice2)
                correct = True
                print(font_colors.OKGREEN + "Car successfully added to car wash"+ font_colors.ENDC)
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def remove_from_car_wash(self):

        correct = False
        while not correct:
            try:
                choice1 = int(input("Choose a car wash"))
                choice2 = int(input("Choose a car"))
                self.__service.remove_from_car_wash(choice1, choice2)
                correct = True
                print(font_colors.OKGREEN + "Car removed from car wash successfully" + font_colors.ENDC )
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)

    def car_options(self):
        try:
            opt = input("1.Create car\n2.Delete car\n3.Modify car\n4.Show cars")
            self.__service.test_input(opt, 4)
            options = {
                "1": self.create_car,
                "2": self.delete_car,
                "3": self.modify_car,
                "4": self.show_cars,
            }
            options[opt]()
        except ValidationError as exp:
            print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)


    def car_wash_options(self):
        print("1.Create car wash\n2.Delete car wash\n3.Modify car wash\n4.Show all car washes")
        try:
            opt = input("5.Show a specified car wash\n6.Add car to a car wash\n7.Remove a car from a car wash")
            self.__service.test_input(opt, 7)
            options = {
                "1": self.create_car_wash,
                "2": self.delete_car_wash,
                "3": self.modify_car_wash,
                "4": self.view_all_car_wash,
                "5": self.view_car_wash,
                "6": self.add_to_car_wash,
                "7": self.remove_from_car_wash,
            }
            options[opt]()

        except ValidationError as exp:
            print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)


    def run(self):
        while True:
            try:
                print("Choose an option:\n1.Car options \n2.Car wash options \n3.Exit")
                option = input()
                self.__service.test_input(option, 3)
                menu = {
                    "1": self.car_options,
                    "2": self.car_wash_options,
                    "3": exit

                }
                menu[option]()
            except ValidationError as exp:
                print(font_colors.FAIL + "An error has occured: " + str(exp) + font_colors.ENDC)
