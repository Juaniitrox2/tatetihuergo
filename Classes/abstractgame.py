from abc import ABC

class AbstractBoardGame(ABC):
    def __init__(self) -> None:
        """Crea una instancia de un juego de mesa en base a un tablero"""
        pass

    def start(self) -> None:
        """Empieza el juego"""
        pass

    def reset(self) -> None:
        """Reinicia los valores del juego"""
        pass