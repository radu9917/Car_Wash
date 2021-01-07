from validator.exceptions import ValidationError


class Validator:
    def validate_car(self, car):
        if not str(car.get_id()).isdecimal():
            raise ValidationError("Index is not valid")
        name = car.get_number()
        if name.upper() != name:
            raise ValidationError("Number not in capslock")
        if name.count(" ") < 2:
            raise ValidationError("Number should have 3 parts")
        check_name = name.split(" ")
        if not check_name[0].isalpha():
            raise ValidationError("First part is not alpha")
        if not check_name[1].isdecimal():
            if 3 < len(check_name[1]) < 2:
                raise ValidationError("Second part is not decimal")
        if not check_name[2].isalpha():
            raise ValidationError("Third part is not alpha")
        owner = car.get_owner().replace("-", " ")
        if not owner.isalpha() or not owner.istitle():
            raise ValidationError("Owner's name is not written correctly")
        if len(owner) > 40:
            raise ValidationError("Name too long")

    def validate_car_wash(self,car_wash):
        if not str(car_wash.get_id()).isdecimal():
            raise ValidationError("Index is not valid")
        if len(car_wash.get_name()) > 20:
            raise ValidationError("Name too long")

    def id_find(self, c_list, index):
        found = False
        for c in c_list.get_all():
            if index == int(c.get_id()):
                found = True
        if not found:
            raise ValidationError("Index not found")

    def id_check(self, c_list, index):
        found = False
        for c in c_list.get_all():
            if index == int(c.get_id()):
                found = True
        if found:
            raise ValidationError("Another with the same index exists")

    def option_check(self, opt, max):
        if int(opt) > int(max):
            raise ValidationError("Invalid option")
