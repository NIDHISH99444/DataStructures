#handing payment in bookMyShow

from abc import  ABC,abstractmethod
class PaymentStratergy(ABC):
    @abstractmethod
    def pay(self):
        pass

class CardPaymentStratergy(PaymentStratergy):
    def pay(self,amount):
        print(f"Payment {amount} from Credit Card ")


class CashPaymentStratergy(PaymentStratergy):
    def pay(self,amount):
        print(f"Payment {amount} from Cash")


class PaymentContext:
    def __init__(self,paymentStratergy):
        self.paymentStratergy=paymentStratergy

    def setPaymentStratergy(self,paymentStratergy):
        self.paymentStratergy = paymentStratergy

    def makePayment(self,amount):
        self.paymentStratergy.pay(amount)


cardPaymentStratergy=CardPaymentStratergy()
cashPaymentStratergy=CashPaymentStratergy()
paymentContext=PaymentContext(cardPaymentStratergy)
paymentContext.makePayment(100)
paymentContext.setPaymentStratergy(cashPaymentStratergy)
paymentContext.makePayment(200)

