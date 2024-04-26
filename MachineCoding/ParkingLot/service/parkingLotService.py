from ParkingLot.dto.parkingFloor import ParkingFloor
from ParkingLot.dto.parkingLot import ParkingLot
from ParkingLot.dto.parkingSlot import ParkingSlot
from ParkingLot.enums.displayType import DisplayType
from ParkingLot.enums.parkingSlotStatus import ParkingSlotStatus
from ParkingLot.enums.vehicleType import VehicleType
from ParkingLot.repo.parkingLotRepository import ParkingLotRepository
from ParkingLot.repo.ticketRepository import TicketRepository

from ParkingLot.service.parkingFloorService import ParkingFloorService
from ParkingLot.service.parkingSlotService import ParkingSlotService


class ParkingLotService:
    def __init__(self):
        self.parkingLotList = ParkingLotRepository.getParkingLotList()

    def createParkingLot(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        parkingFloorList = []
        for i in range(no_of_floors):
            parkingSlotList = []
            for j in range(no_of_slots_per_floor):
                parkingSlot = ParkingSlot(str(j + 1), VehicleType.CAR, ParkingSlotStatus.AVAILABLE, parking_lot_id, i + 1)
                if j == 0:
                    parkingSlot.setVehicleType(VehicleType.TRUCK)
                elif j == 1 or j == 2:
                    parkingSlot.setVehicleType(VehicleType.BIKE)
                parkingSlotList.append(parkingSlot)
            parkingFloor = ParkingFloor(i + 1, parking_lot_id, parkingSlotList)
            parkingFloorList.append(parkingFloor)

        parkingLot = ParkingLot(parking_lot_id, no_of_floors, no_of_slots_per_floor, parkingFloorList)
        ParkingLotRepository.getParkingSlotRepositoryMap()[parking_lot_id] = parkingLot
        ParkingLotRepository.getParkingLotList().append(parkingLot)
        print("Created parking lot with", no_of_floors, "floors and", no_of_slots_per_floor, "slots per floor")

    def parkVehicle(self, vehicle):
        parkingLot = self.parkingLotList[0]
        parkingFloorList = parkingLot.getParkingFloorList()
        floorFullCount = 0
        for parkingFloor in parkingFloorList:
            if ParkingFloorService.getFreeSlotsCount(parkingFloor, vehicle.getVehicleType()) > 0:
                allotmentTicket = ParkingFloorService.allotSlot(parkingFloor, vehicle)
                if allotmentTicket:
                    print("Parked vehicle. Ticket ID:", allotmentTicket.getId())
                    break
            else:
                floorFullCount += 1

        if floorFullCount == len(parkingFloorList):
            print("Parking Lot Full")

    def unparkVehicle(self, ticketId):
        parkingLot = self.parkingLotList[0]
        ticket = TicketRepository.getTicketByTicketId(ticketId)
        parkingSlot = ticket.getParkingSlot()
        vehicle = ticket.getVehicle()
        parkingSlotService = ParkingSlotService(parkingSlot)
        parkingSlotService.unallotSlot(parkingSlot, vehicle)
        TicketRepository.deleteTicket(ticketId)
        print("Unparked vehicle with Registration Number:", vehicle.getRegNo(), "and Color:", vehicle.getColor())

    def display(self, displayType, vehicleType):
        parkingLot = self.parkingLotList[0]
        parkingFloorList = parkingLot.getParkingFloorList()
        for parkingFloor in parkingFloorList:
            if displayType == DisplayType.free_count:
                freeSlotsCount = ParkingFloorService.getFreeSlotsCount(parkingFloor, vehicleType)
                print("No. of free slots for", vehicleType, "on Floor", parkingFloor.getFloorNumber(), ":", freeSlotsCount)
            elif displayType == DisplayType.free_slots:
                print("Free slots for", vehicleType, "on Floor", parkingFloor.getFloorNumber(), ":", end=" ")
                ParkingFloorService.getFreeSlots(parkingFloor, vehicleType)
                print()
            elif displayType == DisplayType.occupied_slots:
                print("Occupied slots for", vehicleType, "on Floor", parkingFloor.getFloorNumber(), ":", end=" ")
                ParkingFloorService.getOccupiedSlots(parkingFloor, vehicleType)
                print()
