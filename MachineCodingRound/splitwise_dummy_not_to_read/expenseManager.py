
from splitwise.expenseService import ExpenseService


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.user_map = {}
        self.balance_sheet = {}

    def add_user(self, user):
        self.user_map[user.get_id()] = user
        self.balance_sheet[user.get_id()] = {}

    def add_expense(self, expense_type, amount, paid_by, splits, expense_metadata):
        expense = ExpenseService.create_expense(expense_type, amount, self.user_map[paid_by], splits, expense_metadata)
        self.expenses.append(expense)
        for split in expense.get_splits():
            paid_to = split.get_user().get_id()
            balances = self.balance_sheet[paid_by]
            balances[paid_to] = balances.get(paid_to, 0.0) + split.get_amount()

            balances = self.balance_sheet[paid_to]
            balances[paid_by] = balances.get(paid_by, 0.0) - split.get_amount()

    def show_balance(self, user_id):
        is_empty = True
        for user, balance in self.balance_sheet[user_id].items():
            if balance != 0:
                is_empty = False
                self.print_balance(user_id, user, balance)

        if is_empty:
            print("No balances")

    def show_balances(self):
        is_empty = True
        for user, balances in self.balance_sheet.items():
            for other_user, balance in balances.items():
                if balance > 0:
                    is_empty = False
                    self.print_balance(user, other_user, balance)

        if is_empty:
            print("No balances")

    def print_balance(self, user1, user2, amount):
        user1_name = self.user_map[user1].get_name()
        user2_name = self.user_map[user2].get_name()
        if amount < 0:
            print(user1_name + " owes " + user2_name + ": " + str(abs(amount)))
        elif amount > 0:
            print(user2_name + " owes " + user1_name + ": " + str(abs(amount)))
