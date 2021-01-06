class Car:
    def __init__(self, index, number, owner):
        self.__id = index
        self.__number = number
        self.__owner = owner

    # Getters
    def get_id(self):
        return self.__id

    def get_number(self):
        return self.__number

    def get_owner(self):
        return self.__owner

    # Setters
    def set_id(self, index):
        self.__id = index

    def set_number(self, number):
        self.__number = number

    def set_owner(self, owner):
        self.__owner = owner

    def __str__(self):
        return self.__owner + " -> " + str(self.__number)

    def __eq__(self, other):
        if self.__id != other.get_id():
            return False
        if self.__owner != other.get_owner():
            return False
        if self.__number != other.get_number():
            return False
        return True
