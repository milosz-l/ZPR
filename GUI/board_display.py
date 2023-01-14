"""Module responsible for board display management and the class BoardWindow."""

from time import sleep
from typing import List
import pygame

try:
    from build.Debug import generatedBoardEngineModuleName
except ModuleNotFoundError or ImportError:  # pylint: disable=binary-op-exception
    from build import generatedBoardEngineModuleName

CELL_SIZE = 15


class BoardWindow:
    """
    Class representing a window with board to be displayed.
    """

    def __init__(
        self, height: int, width: int, states: int, cell_size: int = CELL_SIZE
    ):
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
        for y_val in range(self.height):
            for x_val in range(self.width):
                new_rect = pygame.Rect(
                    x_val * self.cell_size,
                    y_val * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                print(x_val, y_val)
                print("new rect = ", new_rect)
                pygame.draw.rect(self.window, self.colors[new_board[y_val][x_val]], new_rect)

    def save_as_img(self, name: str) -> None:
        """
        Saves displayed board as PNG image.

        Args:
            name:   Desired name of the file.
        """
        pygame.image.save(self.window, f"{name}.png")


def randomize_board(
    engine: generatedBoardEngineModuleName, num_of_random_cells: int
) -> List[List[int]]:
    """
    Returns board with given number of randomized cells

    Args:
        engine:     Game engine written in C++
        num_of_random_cells:    How many cells to randomize

    Returns:
        A matrix with elements equivalent to given cell's state.
    """
    engine.randomize_board(num_of_random_cells)
    return engine.get_board()


def calculate_next_state(
    engine: generatedBoardEngineModuleName
) -> List[List[int]]:
    """
    Returns next state of the board.

    Args:
        engine:     Game engine written in C++

    Returns:
        A matrix with elements equivalent to given cell's state.
    """
    print('before calculating next state:')
    engine.print_current_board()
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
    colors = [(0, 0, 0) for _ in range(states)]
    r_col, g_col, b_col = (0, 0, 0)
    for i in range(states):
        colors[i] = (r_col, g_col, b_col)
        b_col += 255 // (states - 1)
    return colors


def main():
    pygame.init()   # pylint: disable=no-member
    states = 5  # TODO: get these values from engine
    height = 4
    width = height
    board = BoardWindow(height, width, states)
    game_engine = generatedBoardEngineModuleName.PySomeClass()
    game_engine.set_parameters(1, states, False, 2, 3, 3, 3, True)

    # set cells for testing
    game_engine.set_cell(1, 2, 1)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    # game_engine.set_cell(3, 3, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # pylint: disable=no-member
                pygame.quit()               # pylint: disable=no-member
                return
        # new_version = randomize_board(game_engine, num_of_random_cells=width*2)
        new_version = calculate_next_state(game_engine)
        print("before error in python")
        board.update(new_version)
        # game_engine.print_current_board()
        sleep(1)
        pygame.display.flip()


if __name__ == "__main__":
    main()
