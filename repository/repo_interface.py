class RepoInterface:
    def get_all(self):
        pass

    def store(self, obj):
        pass

    def get(self, obj_id):
        pass

    def update(self, old_object, new_object):
        pass

    def delete(self, obj_id):
        pass
