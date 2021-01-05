from car_wash import CarWash
from car import Car


def create_car(car_list=None, car_wash_list=None):

    nr = int(input("How many cars do you want to make?"))
    for num in range(nr):
        print("Create car number " + str(num+1))
        index = int(input("Give car index:"))
        number = input("Give car number")
        owner = input("Give car owner")
        car_list.append(Car(index, number, owner))


def show_cars(car_list=None, car_wash_list=None):
    for car in car_list:
        print(car)


def delete_car(car_list=None, car_wash_list=None):
    index = int(input("What car do you want to delete?"))
    i = 0
    for car in car_list:
        if car.get_id() == index:
            car_list.pop(i)
        i += 1


def modify_car(car_list=None, car_wash_list=None):
    index = int(input("What car do you want to modify?"))
    owner = input("Give the owner's name")
    number = input("Give the car's number")
    i = 0
    for car in car_list:
        if car.get_id() == index:
            car_list[i].set_number(number)
            car_list[i].set_owner(owner)
        i += 1


def view_all_car_wash(car_list=None, car_wash_list=None):
    for car_wash in car_wash_list:
        print(car_wash)


def view_car_wash(car_list=None, car_wash_list=None):
    choice = int(input("Choose a car wash"))
    i = 0
    for car_wash in car_wash_list:
        if choice == car_wash.get_id():
            print(car_wash_list[i])
        i += 1


def rename_car_wash(car_list=None, car_wash_list=None):
    choice = int(input("Choose a car wash to rename:"))
    name = input("Choose the name for the car wash")
    for car_wash in car_wash_list:
        if choice == car_wash.get_id():
            car_wash.set_name(name)


def add_to_car_wash(car_list=None, car_wash_list=None):
    choice1 = int(input("Choose a car wash"))
    choice2 = int(input("Choose the car you want to be added"))
    for car_wash in car_wash_list:
        if choice1 == car_wash.get_id():
            for car in car_list:
                if choice2 == car.get_id():
                    car_wash.add_car(car)


def remove_from_car_wash(car_list=None, car_wash_list=None):
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
        menu[option](car_list, car_wash_list)


main()

