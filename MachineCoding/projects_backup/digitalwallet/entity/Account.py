

from decimal import Decimal

from projects_backup.digitalwallet.entity.user import User
from projects_backup.digitalwallet.util.AccountNumberGenerator import \
    AccountNumberGenerator


class Account:
    def __init__(self, name, amount):
        self.account_number = AccountNumberGenerator.get_next_account_number()

        self.user = User(name)
        self.balance = Decimal(amount)
        self.transactions = []

    def __str__(self):
        return f"Account [accountNumber={self.account_number}, name={self.user.name}, balance={self.balance}, transactions={self.transactions}]"

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        self._transactions = transactions
