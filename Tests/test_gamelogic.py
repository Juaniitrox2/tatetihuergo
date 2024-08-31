#pylint: skip-file
import unittest

from Classes.exceptions import InvalidTileCoordinate, GameFull, GameEmpty, GameStarted
from Classes.tatetilogic import GameLogic
from Classes.player import Player
from Classes.tatetiboard import Board


class TestGameLogic(unittest.TestCase):
    def test_juego_tira_error_con_posicion_de_casilla_invalida(self):
        newgamelogic = GameLogic(Board())
        plr1 = Player("X")

        newgamelogic.add_player(plr1)

        with self.assertRaises(InvalidTileCoordinate):
            newgamelogic.set_player_on_tile(plr1, (5, 12))
    
    def test_juego_tira_error_con_mas_de_dos_jugadores(self):
        newgamelogic = GameLogic(Board())
        plr1 = Player("X")
        plr2 = Player("O")
        plr3 = Player("Y")

        newgamelogic.add_player(plr1)
        newgamelogic.add_player(plr2)
        
        with self.assertRaises(GameFull):
            newgamelogic.add_player(plr3)

    def test_intentar_jugar_sin_suficientes_jugadores(self):
        newgamelogic = GameLogic(Board())

        with self.assertRaises(GameEmpty):
            newgamelogic.play_turn((1, 1))

    def test_intentar_sacar_jugador_cuando_juego_comenzó(self):
        newgamelogic = GameLogic(Board())
        plr1 = Player("X")
        plr2 = Player("O")

        newgamelogic.add_player(plr1)
        newgamelogic.add_player(plr2)

        newgamelogic.play_turn((1, 1))
        with self.assertRaises(GameStarted):
            newgamelogic.remove_player(plr1)

if __name__ == '__main__':
    unittest.main()