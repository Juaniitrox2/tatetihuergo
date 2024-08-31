from Classes.exceptions import InvalidTileCoordinate, OccuppiedTile
from Classes.board import Board
from Classes.player import Player
from abc import ABC

class GameDisplay(ABC):
    def __init__(self, board: Board) -> None:
        self.__board = board

    def draw(self) -> None:
        pass
    
    def get_input(self) -> None:
        """@yields Obtiene un input"""

        pass

    def verify_input(self, x: int, y: int) -> None:
        """Verifica que la coordenada sea válida"""
        
        board_size = self.__board.get_size()
        tiles = self.__board.get_tiles()

        if (x < 0 or x > (board_size[0]-1)) or (y < 0 or y > (board_size[1]-1)):
            raise InvalidTileCoordinate("La posición está fuera de coordenadas")
        
        if not tiles[x][y].is_empty():
            raise OccuppiedTile("Esta casilla ya está ocupada")
        
    
    def show_match_winner(self, winner: Player) -> None:
        """Muestra el ganador de la partida"""

        pass

    def show_match_draw(self) -> None:
        """Muestra cuando la partida se empató"""

        pass