"""Define todas las excepciones o errores que suceden en el código"""

class InvalidGivenPlayer(Exception):
    """Error ocurrente cuando los jugadores entregados no son jugadores válidos"""
    def __init__(self, message):
        self.message = message

class InvalidTileCoordinate(Exception):
    """Error que ocurre cuando la coordenada está fuera de los bordes del tablero"""
    def __init__(self, message):
        self.message = message

class OccuppiedTile(Exception):
    """Error levantado cuando la casilla ya está ocupada"""
    def __init__(self, message):
        self.message = message

class GameFull(Exception):
    """Error levantado cuando el juego está lleno"""
    def __init__(self, message):
        self.message = message

class GameStarted(Exception):
    """Error levantado cuando la partida ya empezó"""
    def __init__(self, message):
        self.message = message

class GameEmpty(Exception):
    """Error levantado cuando el juego está vacío"""

    def __init__(self, message):
        self.message = message
