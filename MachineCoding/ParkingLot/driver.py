from ParkingLot.constants.commands import Commands
from ParkingLot.enums.displayType import DisplayType
from ParkingLot.enums.vehicleType import VehicleType
from ParkingLot.service.inMemoryService import InMemoryService
from ParkingLot.service.parkingLotService import ParkingLotService
from ParkingLot.util.vehicleUtil import VehicleUtil


def main():
    inMemoryService = InMemoryService()
    parkingLotService = ParkingLotService()

    while True:
        inp = input().strip().split()
        try:
            command = inp[0]
            if command == Commands.CREATE:
                parkingLotService.createParkingLot(inp[1], int(inp[2]),
                                                   int(inp[3]))
            elif command == Commands.DISPLAY:
                parkingLotService.display(DisplayType[inp[1]],
                                          VehicleType[inp[2]])
            elif command == Commands.PARK:
                parkingLotService.parkVehicle(
                    VehicleUtil.generateVehicleDto(VehicleType[inp[1]], inp[2],
                                                   inp[3]))
            elif command == Commands.UNPARK:
                parkingLotService.unparkVehicle(inp[1])
            elif command == Commands.EXIT:
                exit(0)
            else:
                print("INVALID INPUT")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
