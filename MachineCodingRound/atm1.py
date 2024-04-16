from abc import ABC,abstractmethod
class ATMState(ABC):
    @abstractmethod
    def insertCardState(self,atm):
        pass

    @abstractmethod
    def validatePin(self,atm,pin):
        pass

    @abstractmethod
    def selectOperation(self,atm,operation):
        pass

    @abstractmethod
    def balanceCheck(self,operation):
        pass
    @abstractmethod
    def ejectCard(self):
        pass

class IdleState(ATMState):


    def insertCardState(self,atm):
        print("inserted card here")
        atm.changeState(HasCardState())


    def validatePin(self, atm, pin):
        pass


    def selectOperation(self, atm, operation):
        pass


    def balanceCheck(self, operation):
        pass


    def ejectCard(self):
        pass


class HasCardState(ATMState):


    def insertCardState(self,atm):
        print("inserted card here")


    def validatePin(self, pin):
        if pin ==123:
            print("Validate Pin")
            atm.changeState(SelectOperationState())
        else:
            print("retry Validating Pin")


    def selectOperation(self, atm, operation):
        pass


    def balanceCheck(self, operation):
        pass


    def ejectCard(self):
        pass


class SelectOperationState(ATMState):

    def insertCardState(self, atm):
        print("inserted card suceess")


    def validatePin(self, atm, pin):
        print("validation card success")


    def selectOperation(self,  operation):
        if operation =='balance':
            atm.changeState(BalanceCheckState())


    def balanceCheck(self, operation):
        pass

    def ejectCard(self):
        pass



class BalanceCheckState(ATMState):

    def insertCardState(self, atm):
        print("inserted card suceess")


    def validatePin(self, atm, pin):
        print("validation card success")


    def selectOperation(self,  operation):
        print("already selected")

    def balanceCheck(self):
        print("Balance is 100")

    def ejectCard(self):
        pass


class ATM :
    def __init__(self):
        self.state=IdleState()


    def changeState(self,state):
        self.state=state


    def insertCardState(self):
        self.state.insertCardState(atm)

    def validatePin(self,  pin):
        self.state.validatePin(pin)


    def selectOperation(self,operation):
        self.state.selectOperation(operation)


    def balanceCheck(self):
        self.state.balanceCheck()

    def ejectCard(self):
        pass

atm=ATM()
atm.insertCardState()
atm.validatePin(123)
atm.selectOperation("balance")
atm.balanceCheck()