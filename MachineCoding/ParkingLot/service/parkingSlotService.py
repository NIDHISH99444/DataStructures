from ParkingLot.enums.parkingSlotStatus import ParkingSlotStatus
from ParkingLot.service.ticketService import TicketService


class ParkingSlotService:
    def __init__(self, parkingSlot):
        self.parkingSlot = parkingSlot

    def allotSlot(self, parkingSlot, vehicle):
        parkingSlot.setParkingSlotStatus(ParkingSlotStatus.UNAVAIALBLE)
        ticket = TicketService.generateTicket(parkingSlot, vehicle)
        parkingSlot.setTicket(ticket)
        return ticket

    def unallotSlot(self, parkingSlot, vehicle):
        parkingSlot.setParkingSlotStatus(ParkingSlotStatus.AVAILABLE)
        parkingSlot.setTicket(None)
