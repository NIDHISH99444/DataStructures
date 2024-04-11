from splitwise.models.expense.expense import Expense
from splitwise.models.split.equalSplit import EqualSplit


class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, EqualSplit):
                return False
        return True