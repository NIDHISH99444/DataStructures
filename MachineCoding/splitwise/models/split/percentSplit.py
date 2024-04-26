from splitwise.models.split.split import Split


class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def get_percent(self):
        return self.percent

    def set_percent(self, percent):
        self.percent = percent
