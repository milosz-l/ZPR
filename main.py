from build.Debug import generatedBoardEngineModuleName
from GUI.board_display import main


def print_board(board):
    for row in board:
        print(row)


if __name__ == '__main__':
    # print(dir(generatedBoardEngineModuleName))

    # board = generatedBoardEngineModuleName.PySomeClass()
    # board_state = board.get_board()
    # print(board_state)
    # # board.print_current_board()
    # print()

    # board.set_cell(0, 0, 1)
    # board_state = board.get_board()
    # print(board_state)
    # # board.print_current_board()
    # print()

    # board.set_cell(1, 0, 1)
    # board.set_cell(1, 1, 1)
    # board_state = board.get_board()
    # print(board_state)
    # # board.print_current_board()
    # print()

    # board.calculate_next_state()
    # print("board after calculating next state:")
    # board_state = board.get_board()
    # print(board_state)

    main()  # main() function from board_display
