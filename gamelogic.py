from board import Board
from player import Player
from exceptions import InvalidGivenPlayer, InvalidTileCoordinate, GameFull

class GameLogic:
    def __init__(self, board: Board) -> None:
        self.__board = board
        self.__players = set()

    def set_player_on_tile(self, player: Player, tile: tuple[int, int]):
        """Asigna un jugador a una casilla predeterminada del tablero"""

        if player not in self.__players:
            raise InvalidGivenPlayer('El jugador dado no es parte del juego')

        x = tile[0]
        y = tile[1]

        if (x < 0 or x > (self.__size[0]-1)) or (y < 0 or y > (self.__size[1]-1)):
            raise InvalidTileCoordinate('Coordenada del tablero inválida')

        self.__board.get_tiles()[x][y].assign_player(player)

    def add_player(self, player: Player):
        if len(self.__players) + 1 > 2:
            raise GameFull('El juego está lleno')

        self.__players.add(player)

    def remove_player(self, player: Player):
        self.__players.remove(player)