from enum import Enum
from abc import abstractmethod,ABC
class ATMStates(Enum):
    Idle=1 
    HasCash=2
    SelectOptions=3
    CashWithdraw=4




class BankAccount:
    def __init__(self,accountNumber,pinCode,expiryDate,holderName):
        self.__accountNumber=accountNumber
        self.__pinCode=pinCode
        self.__expiryDate=expiryDate
        self.__holderName=holderName

        
class SavingAccount(BankAccount):
    def __init__(self, accountNumber, pinCode, expiryDate, holderName):
        super().__init__(accountNumber, pinCode, expiryDate, holderName)

    def withdrawLimit():
        pass

class CurrentAccount(BankAccount):
    def __init__(self, accountNumber, pinCode, expiryDate, holderName):
        super().__init__(accountNumber, pinCode, expiryDate, holderName)

    def withdrawLimit():
        pass


class ATMState(ABC):
    @abstractmethod
    def insertCard(self,atm,card): 
        pass

    @abstractmethod
    def authenticatePin(self,atm,card):
        pass

    @abstractmethod
    def selectOption(self,atm,card,optionTypes):
        pass

    @abstractmethod
    def cashWithdrawal(self,atm,card,amount):
        pass

    @abstractmethod
    def transferMmoney(self,atm,card,amount,sender,receiver_account):
        pass

    @abstractmethod
    def returnCard(self):
        pass

    @abstractmethod
    def exit(self,atm):
        pass

class HaltStates(ATMState):

    def insertCard(self,atm,card): 
        pass

    def authenticatePin(self,atm,card):
        pass


    def selectOption(self,atm,card,optionTypes):
        pass

    
    def cashWithdrawal(self,atm,card,amount):
        pass

    def transferMmoney(self,atm,card,amount,sender,receiver_account):
        pass

    def returnCard(self):
        pass

    def exit(self,atm):
        pass
    