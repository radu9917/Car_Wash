from domain.car_wash import CarWash
from domain.car import Car


class Console:
    def __init__(self, service):
        self.__service = service

    def create_car(self):
        nr = int(input("How many cars do you want to make?"))
        while nr > 0:
            print("Create car :")
            index = int(input("Give car index:"))
            number = input("Give car number")
            owner = input("Give car owner")
            car = Car(index, number, owner)
            if self.__service.create_car(car):
                nr -= 1
            else:
                print("Invalid Data")

    def show_cars(self):
        for car in self.__service.get_all_car():
            print(car)

    def delete_car(self):
        index = int(input("What car do you want to delete?"))
        self.__service.delete_car(index)

    def modify_car(self):
        correct = False

        while not correct:
            index = int(input("What car do you want to change?"))
            number = input("Give car number")
            owner = input("Give car owner")
            car = Car(index, number, owner)
            if self.__service.modify_car(car):
                correct = True
            else:
                print("Invalid Data")

    def view_all_car_wash(self):
        for car_wash in self.__service.get_all_car_wash():
            print(car_wash)

    def view_car_wash(self):
        choice = int(input("Choose a car wash"))
        print(self.__service.get_car_wash(choice))

    def rename_car_wash(self):

        j = int(input("Choose a car wash to rename:"))
        name = input("Choose the name for the car wash")
        car_wash = CarWash(j, name)
        self.__service.rename_car_wash(car_wash)

    def add_to_car_wash(self):
        choice1 = int(input("Choose a car wash"))
        choice2 = int(input("Choose the car you want to be added"))
        self.__service.add_to_car_wash(choice1, choice2)

    def remove_from_car_wash(self):
        choice1 = int(input("Choose a car wash"))
        choice2 = int(input("Choose a car"))
        self.__service.remove_from_car_wash(choice1, choice2)

    def car_options(self):
        print("1.Create car\n2.Delete car\n3.Modify car\n4.Show cars")
        options= {
            "1": self.create_car,
            "2": self.delete_car,
            "3": self.modify_car,
            "4": self.show_cars,
            "5": exit
        }

    def car_wash_options(self):
        print("1.Create car wash\n2.Delete car wash\n3.Modify car wash\n4.Show all car washes")

    def run(self):
        car_wash1 = CarWash(1, "At Johnny's")
        car_wash2 = CarWash(2, "Always Clean")
        car_wash3 = CarWash(3, "Wash It")
        car_wash4 = CarWash(4, "Uncle Bob's Car Wash")
        self.__service.add_car_wash(car_wash1)
        self.__service.add_car_wash(car_wash2)
        self.__service.add_car_wash(car_wash3)
        self.__service.add_car_wash(car_wash4)
        while True:
            print("Choose an option:\n1.Create car \n2.Delete car \n3.Modify car")
            print("4.View all car washes\n5.Rename car wash\n6.Add a car to a car wash")
            print("7.Remove a car from a car wash\n8.View car wash\n9.Show cars\n10.Exit")
            option = input()
            menu = {
                "1": self.create_car,
                "2": self.delete_car,
                "3": self.modify_car,
                "4": self.view_all_car_wash,
                "5": self.rename_car_wash,
                "6": self.add_to_car_wash,
                "7": self.remove_from_car_wash,
                "8": self.view_car_wash,
                "9": self.show_cars,
                "10": exit
            }
            menu[option]()
