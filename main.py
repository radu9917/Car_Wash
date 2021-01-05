from car_wash import CarWash
from car import Car

car_wash_list = []
car_list = []


def create_car():

    print("Create car :")
    index = input("Give car index:")
    number = input("Give car number")
    owner = input("Give car owner")
    car_list.append(Car(index, number, owner))


def delete_car():
    index = int(input("What car do you want to delete?"))
    car_list.pop(index)


def modify_car():
    index = int(input("What car do you want to modify?"))
    owner = input("Give the owner's name")
    number = input("Give the car's number")
    car_list[index].set_number(number)
    car_list[index].set_owner(owner)


def view_all_car_wash():
    for car_wash in car_wash_list:
        print(car_wash)


def view_car_wash():
    choice = int(input("Choose a car wash"))
    print(car_wash_list[choice])


def rename_car_wash():
    choice = int(input("Choose a car wash to rename:"))
    name = input("Choose the name for the car wash")
    car_wash_list[choice].set_name(name)


def add_to_car_wash():
    choice1 = input("Choose a car wash")
    choice2 = int(input("Choose the car you want to be added"))
    for car_wash in car_wash_list:
        if choice1 == car_wash.get_id():
            for car in car_list:
                if car.get_id() == choice2:
                    car_wash.add_car(car)


def remove_from_car_wash():
    choice1 = input("Choose a car wash")
    choice2 = int(input("Choose the car you want to be removed"))
    for car_wash in car_wash_list:
        if choice1 == car_wash.get_id():
            car_wash.remove_car(choice2)


def main():

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
        print("7.Remove a car from a car wash\n8.View car wash")
        option = input()
        options = {
            "1": create_car,
            "2": delete_car,
            "3": modify_car,
            "4": view_all_car_wash,
            "5": rename_car_wash,
            "6": add_to_car_wash,
            "7": remove_from_car_wash,
            "8": view_car_wash
        }
        options[option]()


main()
