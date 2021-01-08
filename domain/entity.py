class Entity:
    def __init__(self, entity_id):
        self.__id = entity_id

    def get_id(self):
        return self.__id

    def set_id(self, entity_id):
        self.__id = entity_id
