from Car_Wash import Car_Wash

from Car import Car

option=input("Choose an option:\n 1.Create car \n 2.View Car washes \n 3.Add car in a car wash")
if option =="1":
      print("Create car :")
      id = input("Give car id:")
      number = input("Give car number")
      owner = input("Give car owner")
      Car1 = Car(id, number, owner)

car_wash1 = Car_Wash(1, "At Johnny's", 0)
car_wash2 = Car_Wash(2, "Always Clean", 0)
car_wash3 = Car_Wash(3, "Wash It", 0)
car_wash4 = Car_Wash(4, "Uncle Bob's Car Wash", 0)
if option=="2":
      print(car_wash1.name+" with "+str(car_wash1.cars)+ " cars queued\n")
      print(car_wash2.name+" with "+str(car_wash2.cars)+" queued\n"+car_wash3.name)
      print(" with "+str(car_wash3.cars)+" queued\n"+car_wash4.name+" with "+str(car_wash4.cars)+" queued\n")
if option=="3":
      name=input("Choose a car wash:")
      if name == car_wash1.name:
          car_wash1.adding_car()
      if name == car_wash2.name:
          car_wash2.adding_car()
      if name == car_wash3.name:
          car_wash3.adding_car()
      if name == car_wash4.name:
          car_wash3.adding_car()