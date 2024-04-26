class ParkingLotRepository:
    parkingLotRepositoryMap = {}
    parkingLotList = []

    def __init__(self):
        ParkingLotRepository.parkingLotRepositoryMap = {}
        ParkingLotRepository.parkingLotList = []

    @staticmethod
    def getParkingLotList():
        return ParkingLotRepository.parkingLotList

    @staticmethod
    def getParkingSlotRepositoryMap():
        return ParkingLotRepository.parkingLotRepositoryMap

