"""Declara la clase abstracta del tablero"""

from abc import ABC
from Classes.tile import Tile

class Board(ABC):
    """Un tablero para algún juego de mesa"""
    def __init__(self, x_size: int, y_size: int):
        """Genera un tablero de mesa"""

    def get_tiles(self) -> list[Tile]:
        """Devuelve una lista de todas las casillas del tablero"""

    def get_size(self) -> tuple[int, int, (int | None)]:
        """Devuelve el tamaño del tablero"""
