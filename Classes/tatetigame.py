from Classes.gamelogic import GameLogic
from Classes.consoledisplay import ConsoleDisplay
from Classes.winchecker import WinChecker
from Classes.board import Board
from Classes.player import Player
from Classes.abstractgame import AbstractBoardGame

class TatetiGame(AbstractBoardGame):
    """Juego del Ta-Te-Ti"""

    def __init__(self):
        self.__board = Board(3, 3)
        self.__logic = GameLogic(self.__board)
        self.__display = ConsoleDisplay(self.__board)
        self.__win_checker = WinChecker(self.__board)

    def start(self):
        """Inicia el juego del Ta-Te-Ti con la lógica y el display especificados"""

        print(f'\nJUEGO DEL TA-TE-TI POR \033[0;33mJUAN IGNACIO DRAGAN\033[0m\nLab. Programación Orientada a Objetos\n')

        # setea jugadores
        player1 = Player(f"\033[0;31mX\033[0m")
        player2 = Player(f"\033[0;34mO\033[0m")

        self.__logic.add_player(player1)
        self.__logic.add_player(player2)
        
        Winner = self.__check_winner()
        while Winner == None:
            self.__draw_board()

            Input = self.__get_input()
            if Input == 'q':
                quit()

            self.__logic.play_turn(Input)
            Winner = self.__check_winner()

        if Winner == 'Draw':
            self.__display.show_match_draw()
        else:
            self.__display.show_match_winner(Winner)

        self.__draw_board()
        
    def reset(self):
        self.__logic.reset()

    def __draw_board(self):
        """Método interno para mostrar el tablero actual utilizando la implementación"""

        self.__display.draw()

    def __get_input(self) -> tuple[int, int]:
        return self.__display.get_input(self.__logic.get_current_turn_player())
    
    def __check_winner(self) -> (Player | None):
        return self.__win_checker.check_winner()
        
