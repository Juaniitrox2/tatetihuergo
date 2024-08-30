class InvalidGivenPlayer(Exception):
    def __init__(self, message):
        self.message = message

class InvalidTileCoordinate(Exception):
    def __init__(self, message):
        self.message = message

class GameFull(Exception):
    def __init__(self, message):
        self.message = message