"""Module responsible for invoking main function from user_options that starts user interface."""

from GUI.user_options import main

def print_board(board):
    """
    Function for printing provided board.
    Useful for debugging.
    """
    for row in board:
        print(row)


if __name__ == "__main__":
    main()
