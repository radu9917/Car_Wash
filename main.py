from car_wash import CarWash
from car import Car

car_wash_list = []
car = None


def create_car():
    global car
    print("Create car :")
    index = input("Give car index:")
    number = input("Give car number")
    owner = input("Give car owner")
    car = Car(index, number, owner)


def view_all_car_wash():
    for car_wash in car_wash_list:
        print(car_wash)


def choose_wash():
    choice = int(input("Choose a car wash"))
    for car_wash in car_wash_list:
        if choice == car_wash.get_id():
            car_wash.add_car(car)


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
        option = input("Choose an option:\n 1.Create car \n 2.View Car washes \n 3.Add car in a car wash")
        options = {
            "1": create_car,
            "2": view_all_car_wash,
            "3": choose_wash
        }
        options[option]()


main()
