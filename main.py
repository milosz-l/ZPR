

def print_board(board):
    for row in board:
        print(row)


if __name__ == '__main__':
    board = [['1', '0'],
             ['1', '1'],]
    
    board_has_changed = True
    while board_has_changed:
        print('new board:')
        print_board(board)
        old_board = board
        # board = BoardEngine.calculate_new_board(board)
        if board == old_board:
            break

    print('no changes in board')
