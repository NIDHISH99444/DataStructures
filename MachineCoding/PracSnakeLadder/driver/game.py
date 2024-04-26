from PracSnakeLadder.entity.ladder import Ladder
from PracSnakeLadder.entity.player import Player
from PracSnakeLadder.entity.snake import Snake
from PracSnakeLadder.services.snakeLadderService import SnakeLadderService

#adding snake

#snakes
snakes = []
snakes.append(Snake(99,10))
snakes.append(Snake(84,65))
snakes.append(Snake(75,35))
snakes.append(Snake(66,23))
snakes.append(Snake(24,12))
snakes.append(Snake(18,3))
#ladders
ladders = []
ladders.append(Ladder(7,21))
ladders.append(Ladder(19,89))
ladders.append(Ladder(27,83))
ladders.append(Ladder(31,78))
ladders.append(Ladder(47,68))
ladders.append(Ladder(57,87))
ladders.append(Ladder(76,98))
#player
players = []
players.append(Player(1,'Pawan'))
players.append(Player(2,'Abhinav'))
players.append(Player(3,'Gyan'))
players.append(Player(4,'Divyank'))


snakeLadderService=SnakeLadderService()
snakeLadderService.setSnakes(snakes)
snakeLadderService.setLadders(ladders)
snakeLadderService.setPlayers(players)

snakeLadderService.startGame()