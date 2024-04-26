from datetime import datetime

class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.date = datetime.now()
    #
    # def __str__(self):
    #     return f"Transaction [from={self.from_account}, to={self.to_account}, amount={self.amount}, date={self.date}]"

    @property
    def from_account(self):
        return self._from_account

    @from_account.setter
    def from_account(self, from_account):
        self._from_account = from_account

    @property
    def to_account(self):
        return self._to_account

    @to_account.setter
    def to_account(self, to_account):
        self._to_account = to_account

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date
