from ParkingLot.dto.ticket import Ticket
from ParkingLot.repo.ticketRepository import TicketRepository


class TicketService:
    @staticmethod
    def generateTicket(parkingSlot, vehicle):
        ticket_id = TicketService.generateTicketId(parkingSlot)
        ticket = Ticket(ticket_id, parkingSlot, vehicle)
        TicketRepository.getTicketMap()[ticket_id] = ticket
        return ticket

    @staticmethod
    def generateTicketId(parkingSlot):
        return str(parkingSlot.getParkingLot()) + "_" + str(parkingSlot.getParkingFloor()) + "_" + str(parkingSlot.getId())

    @staticmethod
    def getTicketByTicketId(ticketId):
        ticket_map = TicketRepository.getTicketMap()
        if ticketId not in ticket_map:
            raise RuntimeError("INVALID TICKET")
        return ticket_map[ticketId]

    @staticmethod
    def deleteTicket(ticketId):
        ticket_map = TicketRepository.getTicketMap()
        if ticketId in ticket_map:
            del ticket_map[ticketId]
