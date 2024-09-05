"""Define la clase principal de una Instancia del juego del Ta-Te-Ti"""

from Classes.tatetilogic import TatetiLogic
from Classes.consoledisplay import ConsoleDisplay
from Classes.tatetiwinchecker import TatetiWinChecker
from Classes.tatetiboard import TatetiBoard
from Classes.player import Player
from Classes.abstractgame import AbstractBoardGame


class TatetiGame(AbstractBoardGame):
    """Juego del Ta-Te-Ti"""

    def __init__(self):
        self.__board = TatetiBoard(3, 3)
        self.__logic = TatetiLogic(self.__board)
        self.__display = ConsoleDisplay(self.__board)
        self.__win_checker = TatetiWinChecker(self.__board)

    def start(self):
        """Inicia el juego del Ta-Te-Ti con la lógica y el display especificados"""

        print(
            f'\nJUEGO DEL TA-TE-TI POR \033[0;33mJUAN IGNACIO DRAGAN\033[0m\nLab. Programación Orientada a Objetos\n')

        # setea jugadores
        player1 = Player(self.__display.get_player_icon(1))
        player2 = Player(self.__display.get_player_icon(2))

        self.__logic.add_player(player1)
        self.__logic.add_player(player2)

        winner = self.__check_winner()
        while winner is None:
            self.__draw_board()

            player_input = self.__get_input()
            if player_input == 'q':
                quit()

            self.__logic.play_turn(player_input)
            winner = self.__check_winner()

        if winner == 'Draw':
            self.__display.show_match_draw()
        else:
            self.__display.show_match_winner(winner)

        self.__draw_board()

    def reset(self):
        self.__logic.reset(self.__board)

    def __draw_board(self):
        """Método interno para mostrar el tablero actual utilizando la implementación"""

        self.__display.draw()

    def __get_input(self) -> tuple[int, int]:
        return self.__display.get_input(self.__logic.get_current_turn_player())

    def __check_winner(self) -> (Player | None):
        return self.__win_checker.check_winner()
