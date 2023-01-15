import pytest
from GUI.board_display import BoardWindow

try:
    from build.Debug import BoardEngine
except ModuleNotFoundError or ImportError:
    from build import BoardEngine

BOARD_SIZE = 50


def test_pybind():
    """
    Tests whether connection with C++ module works and checks if returned gameboard's type is correct.
    """
    game_engine = BoardEngine.BoardEngine()
    gameboard = game_engine.get_board()
    assert isinstance(gameboard, list)


def test_nm_neighbourhood():
    """
    Test NM neighbourhood.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "NM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 1)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 3, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 2


def test_mm_neighbourhood():
    """
    Test MM neighbourhood.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "MM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 1)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 3, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_left_upper_corner():
    """
    tests left upper corner of the board
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "NM")
    game_engine.set_cell(0, 0, 1)
    game_engine.set_cell(0, 1, 1)
    game_engine.set_cell(1, 0, 1)
    first_state = game_engine.get_board()[0][0]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[0][0]
    assert second_state == 2


def test_right_upper_corner():
    """
    tests right upper corner of the board
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "NM")
    game_engine.set_cell(0, BOARD_SIZE-1, 1)
    game_engine.set_cell(0, BOARD_SIZE-2, 1)
    game_engine.set_cell(1, BOARD_SIZE-1, 1)
    first_state = game_engine.get_board()[0][BOARD_SIZE-1]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[0][BOARD_SIZE-1]
    assert second_state == 2


def test_left_lower_corner():
    """
    tests left lower corner of the board
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "NM")
    game_engine.set_cell(BOARD_SIZE-1, 0, 1)
    game_engine.set_cell(BOARD_SIZE-1, 1, 1)
    game_engine.set_cell(BOARD_SIZE-2, 0, 1)
    first_state = game_engine.get_board()[BOARD_SIZE-1][0]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[BOARD_SIZE-1][0]
    assert second_state == 2


def test_right_lower_corner():
    """
    tests right lower corner of the board
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 9, 3, 9, "NM")
    game_engine.set_cell(BOARD_SIZE-1, BOARD_SIZE-1, 1)
    game_engine.set_cell(BOARD_SIZE-1, BOARD_SIZE-2, 1)
    game_engine.set_cell(BOARD_SIZE-2, BOARD_SIZE-1, 1)
    first_state = game_engine.get_board()[BOARD_SIZE-1][BOARD_SIZE-1]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[BOARD_SIZE-1][BOARD_SIZE-1]
    assert second_state == 2


def test_cell_born():
    """
    Tests whether cell is being born.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 3)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 1)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 1)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 1


def test_bmax():
    """
    Tests whether bmax condition (not met) will prevent cell from being born.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 1)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 1)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 1)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_bmin():
    """
    Tests whether bmin condition (not met) will prevent cell from being born.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 4)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 1)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 4)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_cell_survives_and_increments():
    """
    Tests whether a cell survives and increments itself as it should be
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 3)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    game_engine.set_cell(2, 3, 1)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 1)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 2


def test_smin():
    """
    Tests whether smin condition (not met) will prevent a cell from surviving
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 3)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    game_engine.set_cell(2, 3, 0)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 2)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_count_middle():
    """
    Tests whether counting middle works
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, True, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 3)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 1)
    game_engine.set_cell(2, 3, 0)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 2)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 1
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 2


def test_count_middle2():
    """
    Tests whether counting middle works
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, True, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 2)
    game_engine.set_cell(1, 2, 3)
    game_engine.set_cell(1, 3, 4)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 2)
    game_engine.set_cell(2, 3, 0)
    game_engine.set_cell(3, 1, 2)
    game_engine.set_cell(3, 2, 2)
    game_engine.set_cell(3, 3, 4)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 2
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 1


def test_nm_neighbourhood_in_bigger_range():
    """
    Test NM neighbourhood in range bigger than 1.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(2, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 2)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 0)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 3, 3)
    game_engine.set_cell(4, 4, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 1


def test_mm_neighbourhood_in_bigger_range():
    """
    Test MM neighbourhood in range bigger than 1.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(2, 5, False, 2, 3, 3, 3, "MM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 2)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 0)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 3, 3)
    game_engine.set_cell(4, 4, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_mm_neighbourhood_in_bigger_range2():
    """
    Test MM neighbourhood in range bigger than 1.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(2, 5, False, 2, 3, 3, 3, "MM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 2)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 0)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 3, 1)
    game_engine.set_cell(4, 4, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 1


def test_mm_neighbourhood_in_bigger_range3():
    """
    Test MM neighbourhood in range bigger than 1.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(2, 5, False, 2, 3, 3, 3, "MM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 2)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 0)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(2, 4, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 1


def test_mm_neighbourhood_in_bigger_range4():
    """
    Test MM neighbourhood in range bigger than 1.
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(2, 5, False, 2, 3, 3, 3, "MM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 2)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 2)
    game_engine.set_cell(2, 2, 0)
    game_engine.set_cell(2, 3, 4)
    game_engine.set_cell(3, 1, 0)
    game_engine.set_cell(3, 2, 0)
    game_engine.set_cell(3, 4, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 0
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 0


def test_decrementation():
    """
    Tests whether cell decrementation works
    """
    game_engine = BoardEngine.BoardEngine()
    game_engine.set_parameters(1, 5, False, 2, 3, 3, 3, "NM")
    game_engine.set_cell(1, 1, 1)
    game_engine.set_cell(1, 2, 1)
    game_engine.set_cell(1, 3, 1)
    game_engine.set_cell(2, 1, 1)
    game_engine.set_cell(2, 2, 4)
    game_engine.set_cell(2, 3, 1)
    game_engine.set_cell(3, 1, 1)
    game_engine.set_cell(3, 2, 1)
    game_engine.set_cell(3, 3, 1)
    first_state = game_engine.get_board()[2][2]
    assert first_state == 4
    game_engine.calculate_next_state()
    second_state = game_engine.get_board()[2][2]
    assert second_state == 3
