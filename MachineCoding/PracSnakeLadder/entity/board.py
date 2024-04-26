class Board :

    def __init__(self,size):
        self.size=size
        self.snakeList=[]
        self.ladderList=[]
        self.playerCurrentPosition={}

    def getSize(self):
        return  self.size

    def setSize(self,size):
        self.size=size

    def getSnakeList(self):
        return self.snakeList

    def setSnakeList(self, snakeList):
        self.snakeList = snakeList

    def getLadderList(self):
        return self.ladderList

    def setLadderList(self, ladderList):
        self.ladderList = ladderList

    def getPlayerCurrentPosition(self):
        return self.playerCurrentPosition

    def setPlayerCurrentPosition(self, playerCurrentPosition):
        self.playerCurrentPosition = playerCurrentPosition

