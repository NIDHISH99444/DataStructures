from DigitalWalletTry.entity.user import User
from DigitalWalletTry.util.generateRandomNumber import GenerateRandomNumber


class Account:
    def __init__(self, name, amount):
        self.accountNumber = GenerateRandomNumber.generateNumber()
        self.user = User(name)
        self.balance = amount
        self.transactions = []

    def getAccountNumber(self):
        return self.accountNumber

    def setAccountNumber(self, accountNumber):
        self.accountNumber = accountNumber

    def getUser(self):
        return self.name

    def setUser(self,name):
        self.name=name

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getTransactions(self):
        return self.transactions

    def setTransactions(self, transactions):
        self.transactions = transactions