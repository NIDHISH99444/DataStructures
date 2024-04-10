from DigitalWalletTry.dto.walletDto import WalletDto
from DigitalWalletTry.entity.account import Account
from DigitalWalletTry.entity.transaction import Transaction


class WalletService :

    def __init__(self):
        self.dto=WalletDto()


    def createWallet(self,name,amount):
        account=Account(name,amount)
        self.dto.account_map[account.accountNumber]=account
        print(f"Account created for user {name} with account number {account.getAccountNumber()}")

    def validate(self,fromAccountNo, toAccountNo, balance):
        if fromAccountNo == toAccountNo:
            print("Sender and receiver cant be same")
            return False
        elif fromAccountNo not in self.dto.account_map:
            print("Invalid Sender account number")
            return False
        elif toAccountNo not in self.dto.account_map:
            print("Invalid Receiver account number")
            return False
        return True

    def transfer(self, fromAccountNo, toAccountNo, transferAmount):
        if not self.validate(fromAccountNo, toAccountNo, transferAmount):
            return False
        fromAccount=self.dto.account_map.get(fromAccountNo)
        toAccount=self.dto.account_map.get(toAccountNo)
        if fromAccount.balance < transferAmount:
            print("not enough balance")
        fromAccount.balance-=transferAmount
        toAccount.balance+=transferAmount
        transaction=Transaction(fromAccountNo,toAccountNo,transferAmount)
        fromAccount.transactions.append(transaction)
        toAccount.transactions.append(transaction)
        print("transaction success")



    def getAccountStatement(self,accountNumber):
        account=self.dto.account_map.get(accountNumber)
        if not account:
            print("account doesnt exits")
            return
        print(f"Account statement for {accountNumber}")
        print(f"Available balance {account.getBalance()}")
        for transaction in account.transactions:
            print(f"From: {transaction.fromAccount}, To: {transaction.toAccount}, Amount: {transaction.amount}, Date: {transaction.date}")


    def getAccountOverview(self):
        for accNo,account in self.dto.account_map.items():
            print(f"Balance for account Number {accNo} with name {account.user.getName()} is {account.getBalance()}")
