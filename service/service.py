
class Service:
    def __init__(self, car_repo, car_wash_repo, validator):
        self.__car_repo = car_repo
        self.__car_wash_repo = car_wash_repo
        self.__validator = validator

    def create_car(self, car):
        self.__validator.validate_car(car)
        self.__car_repo.store(car)

    def create_car_wash(self, car_wash):
        self.__validator.validate_car_wash(car_wash)
        self.__car_wash_repo.store(car_wash)

    def delete_car(self, index):
        self.__car_repo.delete(index)

    def delete(self, index):
        self.__car_wash_repo.delete(index)

    def modify_car(self, car):
        self.__validator.validate_car(car)
        self.__car_repo.update(car)

    def modify_car_wash(self, car_wash):
        self.__car_wash_repo.update(car_wash)

    def add_to_car_wash(self, car_wash_id, car_id):
        car_wash = self.__car_wash_repo.get(car_wash_id)
        car = self.__car_repo.get(car_id)
        car_wash.add_car(car)
        self.__car_wash_repo.update(self.__car_wash_repo.get(car_wash_id), car_wash)

    def get_car_wash(self, index):
        return self.__car_wash_repo.get(index)

    def remove_from_car_wash(self, car_wash_id, car_id):
        car_wash = self.__car_wash_repo.get(car_wash_id)
        car = self.__car_repo.get(car_id)
        car_wash.remove_car(car)
        self.__car_wash_repo.update(self.__car_wash_repo.get(car_wash_id), car_wash)

    def get_all_car_wash(self):
        return self.__car_wash_repo.get_all()

    def get_all_car(self):
        return self.__car_repo.get_all()