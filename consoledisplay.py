from tile import Tile
from board import Board

class ConsoleDisplay:
    def __init__(self, board: Board):
        self.__board = board

    def draw(self):
        text = "TABLERO ACTUAL:\n------------\n"
        tiles = self.__board.get_tiles()
        
        for x in range(len(tiles)):
            for tile in tiles[x]:
                text = text + tile.get_design() + " "

            text = text + "\n"

        print(text)