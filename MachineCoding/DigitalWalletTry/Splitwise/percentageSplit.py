from workattech.splitwise.models.split import Split

class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
