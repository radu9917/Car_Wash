from validator.exceptions import ValidationError


class Validator:
    def validate_car(self, car):
        name = car.get_number()
        if name.upper() != name:
            raise ValidationError("Number not in capslock")
        if name.count(" ") < 2:
            raise ValidationError("Number should have 3 parts")
        check_name = name.split(" ")
        if not check_name[0].isalpha():
            raise ValidationError("First part is not alpha")
        if not check_name[1].isdecimal():
            if len(check_name[1]) > 3 or len(check_name[1]) < 2:
                raise ValidationError("Second part is not decimal")
        if not check_name[2].isalpha():
            raise ValidationError("Third part is not alpha")
        owner = car.get_owner().replace("-", " ")
        if not owner.isalpha() or not owner.istitle():
            raise ValidationError("Owner's name is not written correctly")
        if len(owner) > 40:
            raise ValidationError("Name too long")

    def validate_car_wash(self,car_wash):
        if len(car_wash.get_name) > 20:
            raise ValidationError("Name too long")

