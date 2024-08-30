from gamelogic import GameLogic
from consoledisplay import ConsoleDisplay
from board import Board

class Game:
    def __init__(self):
        self.__board = Board()
        self.__logic = GameLogic(self.__board)
        self.__display = ConsoleDisplay(self.__board)
