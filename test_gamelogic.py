import unittest

from exceptions import InvalidTileCoordinate
from gamelogic import GameLogic
from player import Player


class TestGameLogic(unittest.TestCase):
    def test_juego_tira_error_con_posicion_de_casilla_invalida(self):
        newboard = GameLogic()
        plr1 = Player("X")

        newboard.add_player(plr1)

        with self.assertRaises(InvalidTileCoordinate):
            newboard.set_player_on_tile(plr1, (5, 12))
    
    def test_juego_tira_error_con_mas_de_dos_jugadores(self):
        newboard = GameLogic()
        plr1 = Player("X")
        plr2 = Player("O")
        plr3 = Player("Y")

        newboard.add_player(plr1)
        newboard.add_player(plr2)
        newboard.add_player(plr3)
    

if __name__ == '__main__':
    unittest.main()