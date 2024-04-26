from decimal import Decimal

from digitalwallet.service.WalletService import WalletService

def main():
    w_service = WalletService()
    while True:
        print("\nOPTIONS:")
        print("1. Create wallet")
        print("2. Transfer Amount")
        print("3. Account Statement")
        print("4. Overview")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("YOU SELECTED CREATE WALLET")
            name = input("Enter name: ")
            amount = Decimal(input("Enter amount: "))
            w_service.create_wallet(name, amount)
        elif choice == 2:
            print("YOU SELECTED TRANSFER")
            from_acc = int(input("Enter SENDER account number: "))
            to_acc = int(input("Enter RECEIVER account number: "))
            amount = Decimal(input("Enter amount: "))
            w_service.transfer(from_acc, to_acc, amount)
        elif choice == 3:
            print("YOU SELECTED ACCOUNT STATEMENT")
            account_num = int(input("Enter account num: "))
            w_service.statement(account_num)
        elif choice == 4:
            print("YOU SELECTED OVERVIEW")
            w_service.overview()
        elif choice == 5:
            print("APPLICATION STOPPED")
            break
        else:
            print("YOU HAVE SELECTED INVALID OPTION. PLEASE REENTER")

if __name__ == "__main__":
    main()
