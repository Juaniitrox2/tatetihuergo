from abc import ABC
from Classes.board import Board
from Classes.player import Player

class WinCheckerAbstract(ABC):
    def __init__(self, board: Board) -> None:
        self.__board = board

    def check_winner(self) -> (Player | None):
        """Chequea el ganador del tablero asignado al juego, usa métodos propios"""
        pass
    
