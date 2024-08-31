from Classes.player import Player

class Tile:
    """Una de todas las casillas dentro del tablero"""

    def __init__(self):
        self.__player_assigned = None

    def assign_player(self, player: Player | None):
        """Asigna un jugador a esta casilla. Por defecto el valor es nulo
        
            Args:
                @player (Player): El jugador en la casilla
        """
        self.__player_assigned = player

    def get_design(self) -> str:
        """Devuelve el diseño de la casilla, el cual varía si la casilla tiene o no un jugador asignado"""

        if self.__player_assigned == None:
            return '□'
        
        return self.__player_assigned.get_tile_design()
    
    def is_empty(self) -> bool:
        return self.get_player() == None
    
    def get_player(self) -> Player:
        return self.__player_assigned
