from gamelogic import GameLogic
from consoledisplay import ConsoleDisplay
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.__board = Board()
        self.__logic = GameLogic(self.__board)
        self.__display = ConsoleDisplay(self.__board)

    def start(self):
        player1 = Player("X")
        player2 = Player("O")

        self.__logic.add_player(player1)
        self.__logic.add_player(player2)

    def draw_board(self):
        self.__display.draw()
