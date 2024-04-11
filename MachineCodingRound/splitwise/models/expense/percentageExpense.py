from splitwise.models.expense.expense import Expense

class PercentExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        total_percent = 100
        sum_split_percent = 0

        for split in self.get_splits():
            if not isinstance(split, PercentSplit):
                return False
            sum_split_percent += split.get_percent()

        return total_percent == sum_split_percent
