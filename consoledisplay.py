from tile import Tile
from board import Board

class ConsoleDisplay:
    def __init__(self, board: Board):
        self.__board = board

    def draw(self):
        text = ""
        for x in range(len(self.__board.get_tiles())):
            for tile in x:
                text = tile.get_design() + " | "

            text = text + "\n"

        print(text)