"""
    Define la clase generadora para un juego de mesa
"""

from abc import ABC

class AbstractBoardGame(ABC):
    """Juego de mesa abstracto el cual puede ser modificado"""

    def __init__(self) -> None:
        """Crea una instancia de un juego de mesa en base a un tablero"""

    def start(self) -> None:
        """Empieza el juego"""

    def reset(self) -> None:
        """Reinicia los valores del juego"""
