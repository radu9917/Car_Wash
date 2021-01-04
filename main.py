from car_wash import CarWash
from car import Car


def main():
    option = input("Choose an option:\n 1.Create car \n 2.View Car washes \n 3.Add car in a car wash")
    if option == "1":
        print("Create car :")
        id = input("Give car id:")
        number = input("Give car number")
        owner = input("Give car owner")
        car1 = Car(id, number, owner)

    car_wash1 = CarWash(1, "At Johnny's", 0)
    car_wash2 = CarWash(2, "Always Clean", 0)
    car_wash3 = CarWash(3, "Wash It", 0)
    car_wash4 = CarWash(4, "Uncle Bob's Car Wash", 0)
    if option == "2":
        print(car_wash1.get_name() + " with " + str(car_wash1.get_cars()) + " cars queued\n")
        print(car_wash2.get_name() + " with " + str(car_wash2.get_cars()) + " queued\n" + car_wash3.get_name())
        print(" with " + str(car_wash3.get_cars()) + " queued\n" + car_wash4.get_name() + " with " + str(car_wash4.get_cars())+" queued\n")
    if option == "3":
        id = input("Choose a car wash:")
        if id == car_wash1.get_id():
            car_wash1.adding_car()
        if id == car_wash2.get_id():
            car_wash2.adding_car()
        if id == car_wash3.get_id():
            car_wash3.adding_car()
        if id == car_wash4.get_id():
            car_wash3.adding_car()

main()
