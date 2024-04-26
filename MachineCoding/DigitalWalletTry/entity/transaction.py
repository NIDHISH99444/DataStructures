

from datetime import  datetime
class Transaction:
    def __init__(self, fromAccount,toAccount,amount):
        self.fromAccount = fromAccount
        self.toAccount = toAccount
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"Transaction [from={self.fromAccount}, to={self.toAccount}, amount={self.amount}, date={self.date}]"

    def getFromAccount(self):
        return self.fromAccount

    def setFromAccount(self,fromAccount):
        self.fromAccount = fromAccount

    def getToAccount(self):
        return self.toAccount

    def setToAccount(self, toAccount):
        self.toAccount = toAccount

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date



