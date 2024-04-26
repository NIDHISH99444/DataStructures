from ParkingLot.dto.vehicle import Vehicle

class VehicleUtil:
    @staticmethod
    def generateVehicleDto(vehicleType, regNo, color):
        return Vehicle(vehicleType, regNo, color)