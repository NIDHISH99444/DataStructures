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
