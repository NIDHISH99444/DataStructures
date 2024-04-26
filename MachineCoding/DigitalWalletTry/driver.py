from DigitalWalletTry.service.walletService import WalletService
from decimal import  Decimal

def main():
    ws=WalletService()
    while True:
        print("\nOPTIONS:")
        print("1. Create wallet")
        print("2. Transfer Amount")
        print("3. Account Statement")
        print("4. Overview")
        print("5. Exit")
        choice=int(input("Enter choice"))
        if choice==1:
            print("You selected create wallet")
            name = input("Enter name")
            amount = int(input("Enter amount"))
            ws.createWallet(name,amount)
        elif choice == 2:
            print("You selected Transfer Amount")
            fromAccount = int(input("Enter SENDER account number"))
            toAccount = int(input("Enter RECEIVER account number"))
            balance = Decimal(input("Enter Amount"))
            ws.transfer(fromAccount, toAccount, balance)
        elif choice == 3:
            print("You selected Account Statement")
            accountNumber=int(input("Enter Account number"))
            ws.getAccountStatement(accountNumber)
        elif choice == 4:
            print("You selected Overview")
            ws.getAccountOverview()
        elif choice == 5:
            break
        else:
            print("Please enter valid input")




if __name__=="__main__":
    main()
