class ParkingLot:
    def __init__(self, id, noOfFloors, noOfSlotsPerFloor, parkingFloorList):
        self.id = id
        self.noOfFloors = noOfFloors
        self.noOfSlotsPerFloor = noOfSlotsPerFloor
        self.parkingFloorList = parkingFloorList

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNoOfFloors(self):
        return self.noOfFloors

    def setNoOfFloors(self, noOfFloors):
        self.noOfFloors = noOfFloors

    def getNoOfSlotsPerFloor(self):
        return self.noOfSlotsPerFloor

    def setNoOfSlotsPerFloor(self, noOfSlotsPerFloor):
        self.noOfSlotsPerFloor = noOfSlotsPerFloor

    def getParkingFloorList(self):
        return self.parkingFloorList

    def setParkingFloorList(self, parkingFloorList):
        self.parkingFloorList = parkingFloorList
