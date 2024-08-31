"""Define la clase winchecker abstracta de la cual heredan otras clases"""

from abc import ABC
from Classes.abstractboard import Board
from Classes.player import Player

class WinCheckerAbstract(ABC):
    """Clase dedicada a confirmar victorias o empates en juegos de mesa"""
    def __init__(self, board: Board) -> None:
        """Genera una nueva instancia de un win-checker"""

    def check_winner(self) -> (Player | None):
        """Chequea el ganador del tablero asignado al juego, usa métodos propios"""
