from typing import List

from .models.expense.equalExpense import EqualExpense
from .models.expense.exactExpense import ExactExpense
from .models.expense.expenseType import ExpenseType
from .models.expense.percentageExpense import PercentExpense


class ExpenseService:
    @staticmethod
    def create_expense(expense_type, amount, paid_by, splits, expense_metadata):
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                split.set_amount((amount * split.get_percent()) / 100.0)
            return PercentExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount * 100 / total_splits, 2)
            for split in splits:
                split.set_amount(split_amount)
            splits[0].set_amount(split_amount + (amount - split_amount * total_splits))
            return EqualExpense(amount, paid_by, splits, expense_metadata)
        else:
            return None
