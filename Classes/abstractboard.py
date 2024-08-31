from abc import ABC
from Classes.tile import Tile

class AbstractBoard(ABC):
    """Un tablero para algún juego de mesa"""

    def get_tiles(self) -> list[Tile]:
        """Devuelve una lista de todas las casillas del tablero"""
        pass

    def get_size(self) -> tuple[int, int, (int | None)]:
        """Devuelve el tamaño del tablero"""
        pass

