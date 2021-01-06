from domain.car_wash import CarWash
from domain.car import Car
from service.service import Service
from repository.repo_car_wash import RepoCarWash
from repository.filerepo_car import FileCarRepo
from tests.test_main import test_main

car_wash_repo1 = RepoCarWash()
car_repo1 = FileCarRepo("cars.txt")
service = Service(car_repo1, car_wash_repo1)


def create_car():
    nr = int(input("How many cars do you want to make?"))
    while nr > 0:
        print("Create car :")
        index = int(input("Give car index:"))
        number = input("Give car number")
        owner = input("Give car owner")
        car = Car(index, number, owner)
        if service.create_car(car):
            nr -= 1
        else:
            print("Invalid Data")


def show_cars():
    for car in service.get_all_car():
        print(car)


def delete_car():
    index = int(input("What car do you want to delete?"))
    service.delete_car(index)


def modify_car():
    correct = False

    while not correct:
        index = int(input("What car do you want to change?"))
        number = input("Give car number")
        owner = input("Give car owner")
        car = Car(index, number, owner)
        if service.modify_car(car):
            correct = True
        else:
            print("Invalid Data")


def view_all_car_wash():
    for car_wash in service.get_all_car_wash():
        print(car_wash)


def view_car_wash():
    choice = int(input("Choose a car wash"))
    print(service.get_car_wash(choice))


def rename_car_wash():

    j = int(input("Choose a car wash to rename:"))
    name = input("Choose the name for the car wash")
    car_wash = CarWash(j, name)
    service.rename_car_wash(car_wash)


def add_to_car_wash():
    choice1 = int(input("Choose a car wash"))
    choice2 = int(input("Choose the car you want to be added"))
    service.add_to_car_wash(choice1, choice2)


def remove_from_car_wash():
    choice1 = int(input("Choose a car wash"))
    choice2 = int(input("Choose a car"))
    service.remove_from_car_wash(choice1, choice2)


def main():

    car_wash1 = CarWash(1, "At Johnny's")
    car_wash2 = CarWash(2, "Always Clean")
    car_wash3 = CarWash(3, "Wash It")
    car_wash4 = CarWash(4, "Uncle Bob's Car Wash")
    service.add_car_wash(car_wash1)
    service.add_car_wash(car_wash2)
    service.add_car_wash(car_wash3)
    service.add_car_wash(car_wash4)
    while True:
        print("Choose an option:\n1.Create car \n2.Delete car \n3.Modify car")
        print("4.View all car washes\n5.Rename car wash\n6.Add a car to a car wash")
        print("7.Remove a car from a car wash\n8.View car wash\n9.Show cars\n10.Exit")
        option = input()
        menu = {
            "1": create_car,
            "2": delete_car,
            "3": modify_car,
            "4": view_all_car_wash,
            "5": rename_car_wash,
            "6": add_to_car_wash,
            "7": remove_from_car_wash,
            "8": view_car_wash,
            "9": show_cars,
            "10": exit
        }
        menu[option]()


test_main()
main()
