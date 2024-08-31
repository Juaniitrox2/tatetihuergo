from Classes.tile import Tile

class Board:
    """El tablero del Ta-Te-Ti, con una lista de casillas representadas en sub listas para simular ejes X e Y"""

    def __init__(self, x_size=3, y_size=3):
        self.__tiles = []
        self.__size =  [x_size, y_size]

        for x in range(x_size):
            self.__tiles.append([])
            
            for y in range(y_size):
                self.__tiles[x].append(Tile())

    def get_tiles(self) -> list[list[Tile]]:
        return self.__tiles
    
    def get_size(self) -> list[int, int]:
        return self.__size
    

