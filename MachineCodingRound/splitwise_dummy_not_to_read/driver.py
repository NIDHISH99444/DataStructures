from splitwise.expenseManager import ExpenseManager
from splitwise.models.expense.expenseType import ExpenseType
from splitwise.models.split.equalSplit import EqualSplit
from splitwise.models.split.exactSplit import ExactSplit
from splitwise.models.split.percentSplit import PercentSplit
from splitwise.models.user import User


class Driver:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.expense_manager.add_user(User("u1", "User1", "gaurav@workat.tech", "9876543210"))
        self.expense_manager.add_user(User("u2", "User2", "sagar@workat.tech", "9876543210"))
        self.expense_manager.add_user(User("u3", "User3", "hi@workat.tech", "9876543210"))
        self.expense_manager.add_user(User("u4", "User4", "mock-interviews@workat.tech", "9876543210"))

    def main(self):
        while True:
            command = input()
            commands = command.split(" ")
            command_type = commands[0]

            if command_type == "SHOW":
                if len(commands) == 1:
                    self.expense_manager.show_balances()
                else:
                    self.expense_manager.show_balance(commands[1])
            elif command_type == "EXPENSE":
                paid_by = commands[1]
                amount = float(commands[2])
                no_of_users = int(commands[3])
                expense_type = commands[4 + no_of_users]
                splits = []
                for i in range(no_of_users):
                    if expense_type == "EQUAL":
                        splits.append(EqualSplit(self.expense_manager.user_map[commands[4 + i]]))
                    elif expense_type == "EXACT":
                        splits.append(ExactSplit(self.expense_manager.user_map[commands[4 + i]], float(commands[5 + no_of_users + i])))
                    elif expense_type == "PERCENT":
                        splits.append(PercentSplit(self.expense_manager.user_map[commands[4 + i]], float(commands[5 + no_of_users + i])))
                self.expense_manager.add_expense(ExpenseType[expense_type], amount, paid_by, splits, None)

if __name__ == "__main__":
    driver = Driver()
    driver.main()
