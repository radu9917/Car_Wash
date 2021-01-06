from domain.car_wash import CarWash
from domain.car import Car
from repository.repo_car import RepoCar
from repository.repo_car_wash import RepoCarWash
import data_check
car_wash_repo = RepoCarWash()
car_repo = RepoCar()


def create_car():
    nr = int(input("How many cars do you want to make?"))
    while nr > 0:
        print("Create car :")
        index = int(input("Give car index:"))
        number = input("Give car number")
        if data_check.number_check(number):
            if data_check.check_car_list(car_repo.get_all(), number):
                owner = input("Give car owner")
                car_repo.store(Car(index, number, owner))
                nr -= 1
            else:
                print("Wrong number")
        else:
            print("Wrong number")


def show_cars():
    for car in car_repo.get_all():
        print(car)


def delete_car():
    index = int(input("What car do you want to delete?"))
    car_repo.delete(index)


def modify_car():
    correct = False
    index = int(input("What car do you want to change?"))
    while not correct:
        number = input("Give car number")
        if data_check.number_check(number):
            if data_check.check_car_list(car_repo.get_all(), number):
                owner = input("Give car owner")
                correct = True

            else:
                print("Wrong number")
        else:
            print("Wrong number")
    car = Car(1, number, owner)
    car_repo.update(index, car)


def view_all_car_wash():
    for car_wash in car_wash_repo.get_all():
        print(car_wash)


def view_car_wash():
    choice = input("Choose a car wash")
    print(car_wash_repo.get(choice))


def rename_car_wash():

    j = int(input("Choose a car wash to rename:"))
    name = input("Choose the name for the car wash")
    car_wash = CarWash(1, name)
    car_wash_repo.update(j, car_wash)


def add_to_car_wash():
    choice1 = int(input("Choose the car you want to be added"))
    choice2 = int(input("Choose a car wash"))
    car_wash_repo.get(choice2).add_car(car_repo.get(choice1))


def remove_from_car_wash():
    choice1 = int(input("Choose a car wash"))
    choice2 = int(input("Choose a car"))
    car_wash_repo.get(choice1).remove_car(car_repo.get(choice2))


def main():

    car_wash1 = CarWash(1, "At Johnny's")
    car_wash2 = CarWash(2, "Always Clean")
    car_wash3 = CarWash(3, "Wash It")
    car_wash4 = CarWash(4, "Uncle Bob's Car Wash")
    car_wash_repo.store(car_wash1)
    car_wash_repo.store(car_wash2)
    car_wash_repo.store(car_wash3)
    car_wash_repo.store(car_wash4)
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
        menu[option]()


main()
