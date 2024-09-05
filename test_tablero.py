#pylint: skip-file
import unittest

from Classes.player import Player
from Classes.tatetiboard import TatetiBoard
from Classes.tile import Tile

class TestTablero(unittest.TestCase):
    def test_tablero_tiene_dimensiones_correctas(self):
        nuevotablero = TatetiBoard(5, 5)

        self.assertEqual([5, 5], nuevotablero.get_size())

    def test_casilla_tiene_jugador(self):
        plr = Player("A")
        nuevacasilla = Tile()

        nuevacasilla.assign_player(plr)
        self.assertEqual(plr, nuevacasilla.get_player())


if __name__ == '__main__':
    unittest.main()