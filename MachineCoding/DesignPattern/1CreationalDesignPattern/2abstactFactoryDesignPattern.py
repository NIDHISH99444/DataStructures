from abc import  ABC,abstractmethod
class Vehicle(ABC) :
    @abstractmethod
    def drive(self):
        pass

class LuxuryVehicle(Vehicle):
    def __init__(self,model):
        self.model=model

    def drive(self):
        print(f'Drives {self.model} luxury vehicle')


class OrdinaryVehicle(Vehicle):
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f'Drives {self.model} ordinary vehicle')

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class LuxuryVehicleFactory(VehicleFactory):
    def create_vehicle(self,model):
        return LuxuryVehicle(model)

class OrdinaryVehicleFactory(VehicleFactory):
    def create_vehicle(self,model):
        return OrdinaryVehicle(model)


luxury_factory=LuxuryVehicleFactory()
luxury_vehicle=luxury_factory.create_vehicle("Mercedes")
luxury_vehicle.drive()


ordinary_factory=OrdinaryVehicleFactory()
ordinary_vehicle=ordinary_factory.create_vehicle("Toyota")
ordinary_vehicle.drive()




