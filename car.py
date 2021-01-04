class Car:
    def __init__(self, index, number, owner):
        self.id = index
        self.number = number
        self.owner = owner

    # Getters
    def get_id(self):
        return self.id

    def get_number(self):
        return self.number

    def get_owner(self):
        return self.owner

    # Setters
    def set_id(self, index):
        self.id = index

    def set_number(self, number):
        self.number = number

    def set_owner(self, owner):
        self.owner = owner

    def __str__(self):
        return self.owner + " -> " + str(self.number)
