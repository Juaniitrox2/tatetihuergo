from gamelogic import GameLogic
from consoledisplay import ConsoleDisplay
from winchecker import WinChecker
from board import Board
from player import Player

class Game:
    """Juego del Ta-Te-Ti"""

    def __init__(self):
        self.__board = Board()
        self.__logic = GameLogic(self.__board)
        self.__display = ConsoleDisplay(self.__board)
        self.__win_checker = WinChecker(self.__board)

    def start(self):
        """Inicia el juego del Ta-Te-Ti con la lógica y el display especificados"""

        print('JUEGO DEL TA-TE-TI POR JUAN IGNACIO DRAGAN\n\n')

        # setea jugadores
        player1 = Player("X")
        player2 = Player("O")

        self.__logic.add_player(player1)
        self.__logic.add_player(player2)
        
        while self.__check_winner() == None:
            self.__draw_board()

            Input = self.__get_input()
            self.__logic.play_turn(Input)

            pass

    def __draw_board(self):
        """Método interno para mostrar el tablero actual utilizando la implementación"""

        self.__display.draw()

    def __get_input(self) -> tuple[int, int]:
        return self.__display.get_input(self.__logic.get_current_turn_player())
    
    def __check_winner(self) -> (Player | None):
        return self.__win_checker.check_winner()
        
