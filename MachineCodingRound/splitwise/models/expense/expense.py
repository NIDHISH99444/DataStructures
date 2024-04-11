from abc import ABC, abstractmethod

class Expense(ABC):
    def __init__(self, amount, paid_by, splits, metadata):
        self.id = None  # ID is not initialized in the constructor
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits
        self.metadata = metadata

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_paid_by(self):
        return self.paid_by

    def set_paid_by(self, paid_by):
        self.paid_by = paid_by

    def get_splits(self):
        return self.splits

    def set_splits(self, splits):
        self.splits = splits

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    @abstractmethod
    def validate(self):
        pass
