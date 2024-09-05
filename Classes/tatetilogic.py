"""
    Genera la lógica especifica para el juego del Ta-Te-Ti
"""

from Classes.abstractboard import Board
from Classes.player import Player
from Classes.exceptions import InvalidGivenPlayer, InvalidTileCoordinate
from Classes.exceptions import GameFull, GameStarted, GameEmpty
from Classes.gamelogic import GameLogic

class TatetiLogic(GameLogic):
    """Lógica del juego del Ta-Te-Ti: Se encarga de asignar jugadores y jugadas"""

    def __init__(self, board: Board) -> None:
        self.__board = board
        self.__players = []
        self.__player_turn_index = 0
        self.__turns_played = 0

    def set_player_on_tile(self, player: Player, tile: tuple[int, int]):
        """Asigna un jugador a una casilla predeterminada del tablero"""

        if player not in self.__players:
            raise InvalidGivenPlayer('El jugador dado no es parte del juego')

        x = tile[0]
        y = tile[1]

        board_size = self.__board.get_size()
        if (x < 0 or x > (board_size[0]-1)) or (y < 0 or y > (board_size[1]-1)):
            raise InvalidTileCoordinate('Coordenada del tablero inválida')

        self.__board.get_tiles()[x][y].assign_player(player)

    def add_player(self, player: Player):
        """Agregar un jugador al juego"""
        if len(self.__players) + 1 > 2:
            raise GameFull('El juego está lleno')

        self.__players.append(player)

    def remove_player(self, player: Player):
        """Remover un jugador de los actuales en el juego"""
        if self.__turns_played > 0:
            raise GameStarted("El juego ya comenzó")

        if len(self.__players) <= 0:
            raise GameEmpty('No hay jugadores en el juego')

        self.__players.remove(player)

    def play_turn(self, player_input: tuple[int, int]):
        """Juega un turno en base a un input previamente ingresado"""

        if len(self.__players) < 2:
            raise GameEmpty("El juego no se puede empezar si no hay 2 jugadores")

        current_player = self.get_current_turn_player()
        self.set_player_on_tile(current_player, player_input)
        self.__turns_played += 1

        #
        if self.__player_turn_index == 0:
            self.__player_turn_index = 1
        else:
            self.__player_turn_index = 0

    def get_current_turn_player(self) -> Player:
        """Devuelve el jugador en el turno actual"""
        if len(self.__players) < 1:
            raise GameEmpty("No hay jugadores")

        return self.__players[self.__player_turn_index]

    def reset(self, board: Board) -> None:
        """Resetea los valores del juego."""
        self.__turns_played = 0
        self.__board = board
