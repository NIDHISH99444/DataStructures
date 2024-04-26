class ParkingSlot:
    def __init__(self, id, vehicleType, parkingSlotStatus, parkingLotId, parkingFloorNumber):
        self.id = id
        self.vehicleType = vehicleType
        self.parkingSlotStatus = parkingSlotStatus
        self.parkingLotId = parkingLotId
        self.parkingFloorNumber = parkingFloorNumber
        self.ticket = None

    def getTicket(self):
        return self.ticket

    def setTicket(self, ticket):
        self.ticket = ticket

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getVehicleType(self):
        return self.vehicleType

    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType

    def getParkingSlotStatus(self):
        return self.parkingSlotStatus

    def setParkingSlotStatus(self, parkingSlotStatus):
        self.parkingSlotStatus = parkingSlotStatus

    def getParkingLotId(self):
        return self.parkingLotId

    def setParkingLotId(self, parkingLotId):
        self.parkingLotId = parkingLotId

    def getParkingFloorNumber(self):
        return self.parkingFloorNumber

    def setParkingFloorNumber(self, parkingFloorNumber):
        self.parkingFloorNumber = parkingFloorNumber
