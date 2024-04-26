from abc import  ABC,abstractmethod

class PriceManagerStratergy(ABC):
    @abstractmethod
    def calculatePrice(self):
        pass

class DistancePriceManagerStratergy(PriceManagerStratergy):
    def calculatePrice(self,distance):
        return distance*0.5

class TimePriceManagerStratergy(PriceManagerStratergy):
    def calculatePrice(self,distance):
        return distance*0.1