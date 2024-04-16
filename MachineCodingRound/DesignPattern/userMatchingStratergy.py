from abc import  ABC,abstractmethod

class DriverManagerStratergy(ABC):
    @abstractmethod
    def findDriver(self):
        pass


class NearestDriverManagerStratergy(DriverManagerStratergy):

    def findDriver(self,location):
        print(f"Nearest Driver found for {location}")
        return "Nearest Driver"

class FastestDriverManagerStratergy(DriverManagerStratergy):

    def findDriver(self,location):
        print(f"Fastest Driver found for {location}")
        return "Fastest Driver"

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

class DriverManagerContext:

    def __init__(self,stratergy):
        self.stratergy=stratergy

    def setStratergy(self,stratergy):
        self.stratergy=stratergy

    def findDriver(self,location):
        return self.stratergy.findDriver(location)

class PricingContext:
    def __init__(self, stratergy):
        self.stratergy = stratergy

    def setStratergy(self, stratergy):
        self.stratergy = stratergy

    def calculatePrice(self, distance):
        return self.stratergy.calculatePrice(distance)


driverManagerStratergy=NearestDriverManagerStratergy()

driverManagerContext=DriverManagerContext(driverManagerStratergy)

print(driverManagerContext.findDriver("mumbai"))


priceManagerStratergy=TimePriceManagerStratergy()
pricingContext=PricingContext(priceManagerStratergy)
print(pricingContext.calculatePrice(20))



