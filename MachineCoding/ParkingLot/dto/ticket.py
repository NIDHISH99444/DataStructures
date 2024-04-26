class Ticket:
    def __init__(self, id, parkingSlot, vehicle):
        self.id = id
        self.parkingSlot = parkingSlot
        self.vehicle = vehicle

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getParkingSlot(self):
        return self.parkingSlot

    def setParkingSlot(self, parkingSlot):
        self.parkingSlot = parkingSlot

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle
