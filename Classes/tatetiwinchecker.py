"""
    Define la clase winchecker para el juego Tateti, heredando de la clase base
    "WinCheckerAbstract"

"""

from Classes.tatetiboard import Board
from Classes.player import Player
from Classes.abstractwinchecker import WinCheckerAbstract

class TatetiWinChecker(WinCheckerAbstract):
    """Una clase encargada de determinar ganadores de un Ta-Te-Ti"""

    def __init__(self, board: Board) -> None:
        self.__board = board

    def check_winner(self) -> (Player | None):
        tiles = self.__board.get_tiles()
        size = self.__board.get_size()

        full_count = 0
        for y in range(size[1]):
            for x in range(size[0]):
                if not tiles[x][y].is_empty():
                    full_count += 1

        for y in range(size[1]):
            last_player = tiles[0][y].get_player()
            horizontal = True
            for x in range(size[0]):
                if tiles[x][y].get_player() != last_player:
                    horizontal = False

            if horizontal and last_player is not None:
                return last_player

        for x in range(size[0]):
            last_player = tiles[0][y].get_player()
            vertical = True
            for y in range(size[1]):
                if tiles[x][y].get_player() != last_player:
                    vertical = False

            if vertical and last_player is not None:
                return last_player

        diag_size = size[0] if size[0] < size[1] else size[1]
        for direccion in range(2):
            diagonal_player = tiles[0][0].get_player()
            diagonal = True
            for x in range(diag_size):
                y = (size[1] - 1 - x) if direccion == 1 else x

                if tiles[x][x].get_player() != diagonal_player:
                    diagonal = False

            if diagonal and diagonal_player is not None:
                return diagonal_player

        if full_count >= (size[0]*size[1]):
            return "Draw"
        return None
