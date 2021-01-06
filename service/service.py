from data_check import number_check
from data_check import check_car_list


class Service:
    def __init__(self, car_repo, car_wash_repo):
        self.__car_repo = car_repo
        self.__car_wash_repo = car_wash_repo

    def add_car_wash(self,car_wash):
        self.__car_wash_repo.store(car_wash)

    def validate_car(self, car):
        car_list = self.__car_repo.get_all()
        if not check_car_list(car_list, car.get_number()):
            return False
        if not number_check(car.get_number()):
            return False

        return True

    def create_car(self, car):
        if self.validate_car(car):
            self.__car_repo.store(car)
            return True
        return False

    def delete_car(self, index):
        self.__car_repo.delete(index)

    def modify_car(self, car):
        if self.validate_car(car):
            self.__car_repo.update(car.get_id())
            return True
        return False

    def rename_car_wash(self, car_wash):
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