from tile import Tile
from board import Board
from player import Player
from exceptions import InvalidTileCoordinate

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

    def get_input(self, player: Player) -> tuple[int, int]:
        valid_input = False

        while not valid_input:
            try:
                print(f'Jugador [{player.get_tile_design()}] ingrese su jugada separada por ; (X;Y):\n')
                player_input = input("->: ").split(';')

                x = int(player_input[0])
                y = int(player_input[0])

                return (x, y)
            except:
                raise InvalidTileCoordinate("Coordenada ingresada es inválida")
