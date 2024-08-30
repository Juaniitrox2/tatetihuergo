from board import Board
from player import Player

class WinChecker:
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
            
            if horizontal:
                return last_player
            
        for x in range(size[0]):
            last_player = tiles[0][y].get_player()
            vertical = True
            for y in range(size[1]):
                if tiles[x][y].get_player() != last_player:
                    vertical = False
            
            if vertical:
                return last_player
        
        if full_count >= 8:
            return "Draw"
        else:
            return None

