import pygame
import random
from time import sleep
# import utils
from typing import List
try:
    from build.Debug import generatedBoardEngineModuleName
except ModuleNotFoundError or ImportError:
    from build import generatedBoardEngineModuleName

CELL_SIZE = 15


class BoardWindow:
    """
    Class representing a window with board to be displayed.
    """

    def __init__(self, height: int, width: int, states: int, cell_size: int = CELL_SIZE):
        """
        Args:
            height:     Height of the window.
            width:      Width of the window.
            states:     Number of cells' states.
            cell_size:  Size of one cell (one dimension is enough as cell is a square).
        """
        self.height = height
        self.width = width
        self.states = states
        self.cell_size = cell_size
        self.window = pygame.display.set_mode((width * cell_size, height * cell_size))
        self.colors = define_colors(states)

    def update(self, new_board: List[List[int]]) -> None:
        """
        Updates displayed board with a new board.

        Args:
            new_board:  A matrix with elements equivalent to given cell's state.
        """
        for y in range(self.height):
            for x in range(self.width):
                new_rect = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.window, self.colors[new_board[y][x]], new_rect)


def new_board(states: int, height: int, width: int, engine: generatedBoardEngineModuleName) -> List[List[int]]:
    """
    Generates new board with random cell states.

    Args:
        states:     Number of cells' states.
        height:     Height of the board.
        width:      Width of the board.
        engine:     Game engine written in C++

    Returns:
        A matrix with elements equivalent to given cell's state.
    """
    # board = [[0 for _ in range(width)] for _ in range(height)]
    # for y in range(height):
    #     for x in range(width):
    #         board[y][x] = random.randint(0, states-1)
    engine.calculate_next_state()
    return engine.get_board()


def define_colors(states: int) -> List[tuple]:
    """
    Sets different colors for cells with different states.

    Args:
        states:     Number of possible cells' states.

    Returns:
        List of colors (in RGB notation) for different states.
    """
    COLORS = [(0, 0, 0) for _ in range(states)]
    R, G, B = (0, 0, 0)
    for i in range(states):
        COLORS[i] = (R, G, B)
        B += 255//(states-1)
    return COLORS


def main():
    pygame.init()
    STATES = 2  # TODO: get these values from engine
    height = 30
    width = 30
    board = BoardWindow(height, width, STATES)
    game_engine = generatedBoardEngineModuleName.PySomeClass()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        new_version = new_board(STATES, height, width, game_engine)
        board.update(new_version)
        sleep(0.5)
        pygame.display.flip()


if __name__ == "__main__":
    main()
