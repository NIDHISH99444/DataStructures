from workattech.splitwise.models.split import Split

class EqualSplit(Split):
    def __init__(self, user):
        super().__init__(user)