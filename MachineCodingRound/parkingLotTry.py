# Question
#https://workat.tech/machine-coding/practice/design-parking-lot-qm6hwq4wkhp8


class Vehicle:
    def __init__(self,type,regNo,color):
        self.type=type
        self.regNo=regNo
        self.color=color


class ParkingSlot:

    def __init__(self,floor,slotNumber):
        self.floor=floor
        self.slotNumber=slotNumber
        self.filled=False
        self.vehicle=None
        self.ticketId=None

    def fillSpot(self,ticketId,vehicleType,vehicleRegNo,vehicleColor):
        self.filled=True
        self.ticketId=ticketId
        self.vehicle=Vehicle(vehicleType,vehicleRegNo,vehicleColor)

class ParkingFloor:

    def __init__(self,floors,spots):
        self.floors={}
        for floor in range(floors):
            for spot in range(spots):
                if floor not in self.floors:
                    self.floors[floor]={}
                self.floors[floor][spot]=ParkingSlot(floor,spot)


class ParkingLot:
    def __init__(self,parkingLotId,noOfFloors,noOfSpots):
        self.id=parkingLotId
        self.floors=int(noOfFloors)
        self.spots=int(noOfSpots)
        self.parkingLot=ParkingFloor(self.floors,self.spots)

    def park(self,vehicleType,registraitonNo,color):
        if vehicleType=='CAR':
            for floor in range(self.floors):
                for slot in range(3,self.spots):
                    if not  self.parkingLot.floors[floor][slot].filled:
                        print(f"Parked vehicle. Car  Ticket ID: {str(self.id)+'_'+str(floor+1)+'_'+str(slot+1)}")
                        self.parkingLot.floors[floor][slot].fillSpot(self.id + "_" + str(floor) + "_" + str(slot),vehicleType,registraitonNo,color)
                        return

        if vehicleType=='TRUCK':
            for floor in range(self.floors):
                for slot in range(1):
                    if not  self.parkingLot.floors[floor][slot].filled:
                        print(f"Parked vehicle. truck Ticket ID: {str(self.id)+'_'+str(floor+1)+'_'+str(slot+1)}")
                        self.parkingLot.floors[floor][slot].fillSpot(self.id + "_" + str(floor) + "_" + str(slot),vehicleType,registraitonNo,color)
                        return

        if vehicleType=='BIKE':
            for floor in range(self.floors):
                for slot in range(1,3):
                    if not  self.parkingLot.floors[floor][slot].filled:
                        print(f"Parked vehicle. bike Ticket ID: {str(self.id)+'_'+str(floor+1)+'_'+str(slot+1)}")
                        self.parkingLot.floors[floor][slot].fillSpot(self.id + "_" + str(floor) + "_" + str(slot),vehicleType,registraitonNo,color)
                        return
        print("not truck splts left")

    def unpark(self,ticetNumber):
        parkingLot,floor,slot=ticetNumber.split('_')
        floor=int(floor)-1
        slot=int(slot)-1

        if self.parkingLot.floors[floor][slot].filled:
            vehicle=self.parkingLot.floors[floor][slot].vehicle
            print(f"Unparked vehicle with Registration Number: {vehicle.regNo} and Color: {vehicle.color}")
            self.parkingLot.floors[floor][slot].filled = False
            self.parkingLot.floors[floor][slot].vehicle = None
            self.parkingLot.floors[floor][slot].ticketId = None

    def freeSlots(self,type,vehicleType):
        if type=='free_slots':
            if vehicleType=='CAR':
                for floor in range(self.floors):
                    slots=[]
                    for slot in range(3,self.spots):
                        if not self.parkingLot.floors[floor][slot].filled:
                            slots.append(slot+1)
                    print(f"Free slots for CAR on Floor {floor+1}: {slots} ")




class Sol:
    def __init__(self):
        self.parkingLots = {}
        self.lastPark=None
    def executerFunction(self):
        completeString=[]
        while True:
            res=[]
            res=list(map(str,input().strip().split()))
            if res[0]=='exit':
                break
            completeString.append(res)
        for entry in completeString:
            if entry[0]=='create_parking_lot':
                newParkingLot=entry[1]
                if newParkingLot not  in self.parkingLots:
                    self.parkingLots[newParkingLot]=ParkingLot(entry[1],entry[2],entry[3])
                    print(f"Created parking lot with {entry[2]} floors and {entry[3]} slots per floor")
                    self.lastPark=newParkingLot
            elif entry[0]=='park_vehicle':
                self.parkingLots[self.lastPark].park(entry[1],entry[2],entry[3])


            elif  entry[0]=='unpark_vehicle':
                self.parkingLots[self.lastPark].unpark(entry[1])
            elif entry[0] == 'display':
                self.parkingLots[self.lastPark].freeSlots(entry[1],entry[2])







s=Sol()
s.executerFunction()




