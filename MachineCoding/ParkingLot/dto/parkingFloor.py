class ParkingFloor:
    def __init__(self, floorNumber, parkingLotId, parkingSlotList):
        self.floorNumber = floorNumber
        self.parkingLotId = parkingLotId
        self.parkingSlotList = parkingSlotList

    def getFloorNumber(self):
        return self.floorNumber

    def setFloorNumber(self, floorNumber):
        self.floorNumber = floorNumber

    def getParkingLotId(self):
        return self.parkingLotId

    def setParkingLotId(self, parkingLotId):
        self.parkingLotId = parkingLotId

    def getParkingSlotList(self):
        return self.parkingSlotList

    def setParkingSlotList(self, parkingSlotList):
        self.parkingSlotList = parkingSlotList
