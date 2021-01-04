from car_wash import CarWash
from car import Car


def main():

    car1 = None
    car_wash1 = CarWash(1, "At Johnny's")
    car_wash2 = CarWash(2, "Always Clean")
    car_wash3 = CarWash(3, "Wash It")
    car_wash4 = CarWash(4, "Uncle Bob's Car Wash")

    while True:
        option = input("Choose an option:\n 1.Create car \n 2.View Car washes \n 3.Add car in a car wash")

        if option == "1":
            print("Create car :")
            index = input("Give car index:")
            number = input("Give car number")
            owner = input("Give car owner")
            car1 = Car(index, number, owner)
            print(car1)


        if option == "2":
            print(car_wash1)
            print(car_wash2)
            print(car_wash3)
            print(car_wash4)
        if option == "3":
            index = int(input("Choose a car wash:"))
            if index == car_wash1.get_id():
                car_wash1.add_car(car1)
            if index == car_wash2.get_id():
                car_wash2.add_car(car1)
            if index == car_wash3.get_id():
                car_wash3.add_car(car1)
            if index == car_wash4.get_id():
                car_wash3.add_car(car1)


main()
