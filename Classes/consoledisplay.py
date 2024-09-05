"""
Define la clase de un display para la consola
"""

from Classes.abstractboard import Board
from Classes.player import Player
from Classes.exceptions import InvalidTileCoordinate, OccuppiedTile
from Classes.gamedisplay import GameDisplay

class ConsoleDisplay(GameDisplay):
    """Una instancia de un display en consola para un juego"""

    def __init__(self, board: Board):
        super().__init__(board)
        self.__board = board

    def draw(self):
        board_text = "\nTABLERO ACTUAL:\n------------\n"
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

    def get_player_icon(self, index: int) -> str:
        """Obtiene el ícono que van a utilizar los jugadores en la partida en base a un índice"""
        player_icon = input(f"Jugador [{index}] ingrese el ícono con el que se representara:\n->: ")

        player_icon = f"\033[0;3{index}m{player_icon[0]}\033[0m"
        return player_icon

    def show_match_winner(self, winner: Player) -> None:
        print('\n\n\n\033[0;31mPARTIDA TERMINADA\033[0m')
        print(f'El ganador del Ta-Te-Ti es:\nJugador [{winner.get_tile_design()}]\n')

    def show_match_draw(self) -> None:
        print('\n\n\n\033[0;31mPARTIDA TERMINADA\033[0m')
        print('El resultado de la partida es:\nEMPATE\n')
