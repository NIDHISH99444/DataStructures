class Vehicle:
    def __init__(self, vehicleType, regNo, color):
        self.vehicleType = vehicleType
        self.regNo = regNo
        self.color = color

    def getVehicleType(self):
        return self.vehicleType

    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType

    def getRegNo(self):
        return self.regNo

    def setRegNo(self, regNo):
        self.regNo = regNo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
