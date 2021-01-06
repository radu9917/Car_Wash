from car_wash import CarWash
from car import Car
from repo import  Repo
import data_check

car_repo = Repo()


def find_car_wash(car_wash_list):
    j = 0
    choice1 = int(input())
    for car_wash in car_wash_list:
        if choice1 == car_wash.get_id():
            return j
        j += 1


def create_car(car_wash_list=None):
    nr = int(input("How many cars do you want to make?"))
    while nr > 0:
        print("Create car :")
        index = int(input("Give car index:"))
        number = input("Give car number")
        if data_check.number_check(number):
            if data_check.check_car_list(car_repo.find_all(), number):
                owner = input("Give car owner")
                car_repo.store(Car(index, number, owner))
                nr -= 1
            else:
                print("Wrong number")
        else:
            print("Wrong number")


def show_cars(car_wash_list=None):
    for index in len(car_repo.find_all):
        print(car_repo.get(index))


def delete_car(car_wash_list=None):
    index = int(input("What car do you want to delete?"))
    car_repo.delete(index)


def modify_car(car_wash_list=None):
    correct = False
    index = int(input("What car do you want to change?"))
    while not correct:
        number = input("Give car number")
        if data_check.number_check(number):
            if data_check.check_car_list(car_repo.find_all(), number):
                owner = input("Give car owner")
                correct = True

            else:
                print("Wrong number")
        else:
            print("Wrong number")
    car = Car(1, number, owner)
    car_repo.update(index, car)


def view_all_car_wash(car_wash_list=None):
    for car_wash in car_wash_list:
        print(car_wash)


def view_car_wash(car_wash_list=None):
    print("Choose a car wash")
    print(car_wash_list[find_car_wash(car_wash_list)])


def rename_car_wash(car_wash_list=None):
    print("Choose a car wash to rename:")
    j = find_car_wash(car_wash_list)
    name = input("Choose the name for the car wash")
    car_wash_list[j].set_name(name)


def add_to_car_wash(car_wash_list=None):
    choice = int(input("Choose the car you want to be added"))
    print("Choose a car wash")
    j = find_car_wash(car_wash_list)
    car_wash_list[j].add_car(car_repo.get(choice))


def remove_from_car_wash(car_wash_list=None):
    choice1 = int(input("Choose a car wash"))
    choice2 = int(input("Choose a car"))
    for car_wash in car_wash_list:
        if choice1 == car_wash.get_id():
            j = 0
            for car in car_wash.cars:
                if car.get_id() == choice2:
                    car_wash.remove_car(j)
                j += 1


def main():
    car_wash_list = []
    car_list = []
    car_wash1 = CarWash(1, "At Johnny's")
    car_wash2 = CarWash(2, "Always Clean")
    car_wash3 = CarWash(3, "Wash It")
    car_wash4 = CarWash(4, "Uncle Bob's Car Wash")
    car_wash_list.append(car_wash1)
    car_wash_list.append(car_wash2)
    car_wash_list.append(car_wash3)
    car_wash_list.append(car_wash4)
    while True:
        print("Choose an option:\n1.Create car \n2.Delete car \n3.Modify car")
        print("4.View all car washes\n5.Rename car wash\n6.Add a car to a car wash")
        print("7.Remove a car from a car wash\n8.View car wash\n9.Show cars")
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
            "9": show_cars
        }
        menu[option](car_wash_list)


main()
