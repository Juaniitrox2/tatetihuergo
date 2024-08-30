from tile import Tile
from board import Board
from player import Player
from exceptions import InvalidTileCoordinate, OccuppiedTile
from gamedisplay import GameDisplay

class ConsoleDisplay(GameDisplay):
    def __init__(self, board: Board):
        super().__init__(board)
        self.__board = board

    def draw(self):
        board_text = "TABLERO ACTUAL:\n------------\n"
        tiles = self.__board.get_tiles()
        size = self.__board.get_size()
        
        for y in range(size[1]):
            for x in range(size[0]):
                tile = tiles[x][y]

                board_text = board_text + tile.get_design() + " "
            board_text = board_text + "\n"

        print(board_text)

    def get_input(self, player: Player) -> tuple[int, int]:
        """@yields Obtiene un input mediante la consola"""

        while True:
            try:
                print(f'Jugador [{player.get_tile_design()}] ingrese su jugada en el siguiente formato [X;Y] (o escriba Q para salir):\n')
                player_input = input("->: ").split(';')

                if player_input[0].lower() == 'q':
                    return 'q'

                x = int(player_input[0]) - 1
                y = int(player_input[1]) - 1

                self.verify_input(x, y)

                return (x, y)
            except InvalidTileCoordinate:
                print("Por favor ingrese una coordenada valida")
            except OccuppiedTile:
                print("Esta casilla ya está ocupada")
            except:
                print('Por favor ingrese valores válidos')

    def show_winner(self, player: Player) -> None:
        print('\n\n\n\032[0;31mPARTIDA TERMINADA\033[0m')
        print(f'El ganador del Ta-Te-Ti es:\nJugador [{player.get_tile_design()}]\n')
