from build.Debug import generatedBoardEngineModuleName


def print_board(board):
    for row in board:
        print(row)


if __name__ == '__main__':
    print(dir(generatedBoardEngineModuleName))

    board = generatedBoardEngineModuleName.PySomeClass()
    board.print_current_board()
    print()

    board.set_cell(0, 0, 1)
    board.print_current_board()
    print()

    board.set_cell(1, 0, 1)
    board.set_cell(1, 1, 1)
    board.print_current_board()
    print()

    board.calculate_next_state()
    print("board after calculating next state:")
    board.print_current_board()

    # board = [['1', '0'],
    #          ['1', '1'], ]

    # board_has_changed = True
    # while board_has_changed:
    #     print('new board:')
    #     print_board(board)
    #     old_board = board
    #     # board = BoardEngine.calculate_new_board(board)
    #     if board == old_board:
    #         break

    # print('no changes in board')
