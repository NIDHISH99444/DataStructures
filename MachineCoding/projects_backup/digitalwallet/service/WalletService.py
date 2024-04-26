from decimal import Decimal



from projects_backup.digitalwallet.dao.WalletDao import WalletDao
from projects_backup.digitalwallet.entity.Account import Account
from projects_backup.digitalwallet.entity.Transaction import Transaction


class WalletService:
    def __init__(self):
        self.dao = WalletDao()

    def create_wallet(self, name, amount):
        account = Account(name, amount)
        self.dao.account_map[account.account_number] = account
        print(f"Account created for user {name} with account number {account.account_number}")

    def transfer(self, from_acc_num, to_acc_num, transfer_amount):
        if not self.validate(from_acc_num, to_acc_num, transfer_amount):
            return

        transaction = Transaction(from_acc_num, to_acc_num, transfer_amount)
        from_account = self.dao.account_map.get(from_acc_num)
        to_account = self.dao.account_map.get(to_acc_num)
        if from_account.balance < transfer_amount:
            print("Insufficient Balance")
            return

        from_account.balance -= transfer_amount
        to_account.balance += transfer_amount
        from_account.transactions.append(transaction)
        to_account.transactions.append(transaction)
        print("Transfer Successful")

    def validate(self, from_acc_num, to_acc_num, transfer_amount):
        if from_acc_num == to_acc_num:
            print("Sender and Receiver cannot be same.")
            return False
        if transfer_amount < Decimal('0.0001'):
            print("Amount too low")
            return False
        if from_acc_num not in self.dao.account_map:
            print("Invalid Sender account number")
            return False
        if to_acc_num not in self.dao.account_map:
            print("Invalid Receiver account number")
            return False
        return True

    def statement(self, account_num):
        account = self.dao.account_map.get(account_num)
        if not account:
            print("Invalid Account Number")
            return
        print(f"Summary for account number: {account_num}")
        print(f"Current Balance: {account.balance}")
        print("Your Transaction History:")
        for transaction in account.transactions:
            print(f"From: {transaction.from_account}, To: {transaction.to_account}, Amount: {transaction.amount}, Date: {transaction.date}")


    def overview(self):
        for acc_num, account in self.dao.account_map.items():
            print(f"Balance for account number {acc_num}: {account.balance}")
