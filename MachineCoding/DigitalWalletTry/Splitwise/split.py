from workattech.splitwise.models.user import User

class Split:
    def __init__(self, user):
        self.user = user
        self.amount = 0.0

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount