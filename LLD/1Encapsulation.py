# Encapsulation is achieved when each object keeps its state private so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.
class Product : 
    def __init__(self) :
        self.__maxPrice=600
    
    def get_price(self):
        print('Maxprice',self.__maxPrice)

    def set_price(self,price):
        self.__maxPrice=price


p=Product();

p.__maxPrice=500
p.get_price()

p.set_price(700)
p.get_price()


