from splitwise.models.expense.expense import Expense

class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        total_amount = self.get_amount()
        sum_split_amount = 0

        for split in self.get_splits():
            if not isinstance(split, ExactSplit):
                return False
            sum_split_amount += split.get_amount()

        return total_amount == sum_split_amount
