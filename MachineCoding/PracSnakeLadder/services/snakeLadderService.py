from PracSnakeLadder.entity.board import Board
from PracSnakeLadder.services.diceRollService import DiceRollService


class SnakeLadderService:

    def __init__(self):
        self.board=Board(100)

    def setSnakes(self,snakes):
        self.board.snakeList=snakes

    def setLadders(self,ladders):
        self.board.ladderList = ladders

    def setPlayers(self,players):
        self.queueList=[]
        self.initialPlayerCount=len(players)
        playerPositionDict={}
        for player in players:
            self.queueList.append(player)
            playerPositionDict[player.getId()]=0

        self.board.playerCurrentPosition=playerPositionDict


    def checkGameComplete(self):
        return  self.initialPlayerCount == len(self.queueList)

    def getDiceCount(self):
        return  DiceRollService().roll()

    def getNexPosition(self,player,nextPosition):
        print(f'Procession player {player.getName()} for position {nextPosition}')
        while True:
            for ladder in self.board.ladderList:
                if nextPosition==ladder.getStart():
                    print(f'Player {player.getName()} found a ladder from {ladder.getStart()} to {ladder.getEnd()}')
                    nextPosition=ladder.getEnd()
                    continue
            for snake in self.board.snakeList:
                if nextPosition==snake.getStart():
                    print(f'Player {player.getName()} found a snake from {snake.getStart()} to {snake.getEnd()}')
                    nextPosition=snake.getEnd()
                    continue
            break
        return nextPosition

    def nextMove(self,player,diceCount):
        currentPosition=self.board.playerCurrentPosition[player.getId()]
        nextPosition = diceCount+ currentPosition
        if nextPosition > self.board.getSize():
            nextPosition=currentPosition
        else:
            nextPosition=self.getNexPosition(player,nextPosition)
        self.board.playerCurrentPosition[player.getId()]=nextPosition
        return nextPosition

    def reachedEndOfBoard(self,position):
        return position == self.board.getSize()



    def startGame(self):
        while self.checkGameComplete():
            diceCount=self.getDiceCount()
            player=self.queueList.pop(0)
            playerPoistion = self.nextMove(player,diceCount)
            if self.reachedEndOfBoard(playerPoistion):
                print(f"Player {player.getName()} won the match")

            else:
                self.queueList.append(player)





