from board import Board
from player import Player

class WinChecker:
    def __init__(self, board: Board) -> None:
        self.__board = board

    def check_winner(self) -> (Player | None):
        return None