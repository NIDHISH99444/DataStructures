from ParkingLot.repo.parkingFloorRepository import ParkingFloorRepository
from ParkingLot.repo.parkingLotRepository import ParkingLotRepository
from ParkingLot.repo.parkingSlotRepository import ParkingSlotRepository
from ParkingLot.repo.ticketRepository import TicketRepository


class InMemoryService:
    def __init__(self):
        self.parkingLotRepository = ParkingLotRepository()
        self.parkingFloorRepository = ParkingFloorRepository()
        self.parkingSlotRepository = ParkingSlotRepository()
        self.ticketRepository = TicketRepository()
