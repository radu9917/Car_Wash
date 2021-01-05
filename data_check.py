from car import Car


def number_check(name):
    if name.upper() != name:
        return False
    check_name = name.split(" ")
    if not check_name[0].isalpha():
        return False
    if not check_name[1].isdecimal():
        if len(check_name[1]) > 3 or len(check_name[1]) < 2:
            return False
    if not check_name[2].isalpha():
        return False
    if check_name[3]:
        return False
    return True


def owner_check(name):
    if not name.title():
        return False


def check_car_list(car_list, number):

    for car in car_list:
        if car.get_number() == number:
            return False
    return True



