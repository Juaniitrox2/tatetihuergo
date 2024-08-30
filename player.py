class Player:
    def __init__(self, tile_design: str):
        self.__design = tile_design

    def get_tile_design(self) -> str:
        """Devuelve el diseño de casilla asignado al jugador"""

        return self.__design
