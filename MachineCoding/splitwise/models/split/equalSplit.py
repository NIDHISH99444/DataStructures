from splitwise.models.split.split import Split


class EqualSplit(Split):
    def __init__(self, user):
        super().__init__(user)
