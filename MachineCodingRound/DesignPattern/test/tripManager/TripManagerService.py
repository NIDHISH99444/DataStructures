
from DesignPattern.test.stratergy.priceMatchingStratergy import \
    DistancePriceManagerStratergy


class PriceMangerService:

    def __init__(self,stratergy):
        self.stratergy=stratergy

    def calculatePrice(self,distance):
        return self.stratergy.calculatePrice(distance)



distancePriceManagerStratergy=DistancePriceManagerStratergy()
priceMangerService=PriceMangerService(distancePriceManagerStratergy)
print(priceMangerService.calculatePrice(10))
