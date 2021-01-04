class Car:
    def __init__(self, id, number, owner):
        self.id = id
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
    def set_id(self, id):
        self.id = id

    def set_number(self, number):
        self.number = number

    def set_owner(self, owner):
        self.owner = owner