import uuid

class User:
    def __init__(self, name):
        self.id = uuid.uuid4().hex
        self.name = name

    def __str__(self):
        return f"User [id={self.id}, name={self.name}]"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
