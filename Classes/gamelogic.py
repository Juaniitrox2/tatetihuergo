"""
    Define la clase GameLogic abstracta, la cual otras clases heredan
"""

from abc import ABC

class GameLogic(ABC):
    """Define una clase gamelogic para la cual otras heredan"""

    def set_player_on_tile(self, player, tile: tuple[int, int]):
        """Define que jugador está en que casilla"""
