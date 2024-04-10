import uuid


class User:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4().hex

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id


