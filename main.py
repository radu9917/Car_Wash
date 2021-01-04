from car_wash import CarWash
from car import Car


car_wash1 = CarWash(1, "At Johnny's")
car_wash2 = CarWash(2, "Always Clean")
car_wash3 = CarWash(3, "Wash It")
car_wash4 = CarWash(4, "Uncle Bob's Car Wash")


def create_car():
    print("Create car :")
    index = input("Give car index:")
    number = input("Give car number")
    owner = input("Give car owner")
    return Car(index, number, owner)


def view_car_wash():
    print(car_wash1)
    print(car_wash2)
    print(car_wash3)
    print(car_wash4)


def choose_wash(car1):
    index = int(input("Choose a car wash:"))
    if index == car_wash1.get_id():
        car_wash1.add_car(car1)
    if index == car_wash2.get_id():
        car_wash2.add_car(car1)
    if index == car_wash3.get_id():
        car_wash3.add_car(car1)
    if index == car_wash4.get_id():
        car_wash3.add_car(car1)


def main():

    car1 = None

    while True:
        option = input("Choose an option:\n 1.Create car \n 2.View Car washes \n 3.Add car in a car wash")

        if option == "1":
           car1 = create_car()
        if option == "2":
            view_car_wash()
        if option == "3":
            choose_wash(car1)


main()
