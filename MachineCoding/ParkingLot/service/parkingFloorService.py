from ParkingLot.enums.parkingSlotStatus import ParkingSlotStatus
from ParkingLot.service.parkingSlotService import ParkingSlotService


class ParkingFloorService:
    @staticmethod
    def getFreeSlotsCount(parkingFloor, vehicleType):
        parkingSlotList = parkingFloor.getParkingSlotList()
        count = sum(1 for parkingSlot in parkingSlotList if parkingSlot.getParkingSlotStatus() == ParkingSlotStatus.AVAILABLE
                    and parkingSlot.getVehicleType() == vehicleType)
        return count

    @staticmethod
    def getFreeSlots(parkingFloor, vehicleType):
        parkingSlotList = parkingFloor.getParkingSlotList()
        freeSlots = [parkingSlot.getId() for parkingSlot in parkingSlotList
                     if parkingSlot.getParkingSlotStatus() == ParkingSlotStatus.AVAILABLE
                     and parkingSlot.getVehicleType() == vehicleType]
        print(','.join(freeSlots))

    @staticmethod
    def getOccupiedSlots(parkingFloor, vehicleType):
        parkingSlotList = parkingFloor.getParkingSlotList()
        occupiedSlots = [parkingSlot.getId() for parkingSlot in parkingSlotList
                         if parkingSlot.getParkingSlotStatus() == ParkingSlotStatus.UNAVAIALBLE
                         and parkingSlot.getVehicleType() == vehicleType]
        print(','.join(occupiedSlots))

    @staticmethod
    def allotSlot(parkingFloor, vehicle):
        parkingSlotList = parkingFloor.getParkingSlotList()
        availableParkingSlots = [parkingSlot for parkingSlot in parkingSlotList
                                 if parkingSlot.getParkingSlotStatus() == ParkingSlotStatus.AVAILABLE
                                 and parkingSlot.getVehicleType() == vehicle.getVehicleType()]
        if availableParkingSlots:
            parkingSlot = availableParkingSlots[0]
            ticket = ParkingSlotService(parkingSlot).allotSlot(parkingSlot, vehicle)
            return ticket
        else:
            return None
