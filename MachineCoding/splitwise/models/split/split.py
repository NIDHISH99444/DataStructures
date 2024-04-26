

class Split:
    def __init__(self, user):
        self.user = user
        self.amount = None

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
