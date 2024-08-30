from board import Board
from player import Player
from exceptions import InvalidGivenPlayer, InvalidTileCoordinate, GameFull, GameStarted, GameEmpty

class GameLogic:
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

        if (x < 0 or x > (self.__size[0]-1)) or (y < 0 or y > (self.__size[1]-1)):
            raise InvalidTileCoordinate('Coordenada del tablero inválida')

        self.__board.get_tiles()[x][y].assign_player(player)

    def add_player(self, player: Player):
        if len(self.__players) + 1 > 2:
            raise GameFull('El juego está lleno')

        self.__players.append(player)

    def remove_player(self, player: Player):
        if self.__turns_played > 0:
            raise GameStarted("El juego ya comenzó")
        
        if len(self.__players) <= 0:
            raise GameEmpty('No hay jugadores en el juego')

        self.__players.remove(player)

    def play_turn(self, input: tuple[int, int]):
        """Juega un turno en base a un input previamente ingresado"""

        if len(self.__players) < 2:
            raise GameEmpty("El juego no se puede empezar si no hay 2 jugadores")
        
        currentPlayer = self.get_current_turn_player()
        self.set_player_on_tile(currentPlayer, input)

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
