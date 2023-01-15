import pytest
from GUI.board_display import BoardWindow

try:
    from build.Debug import BoardEngine
except ModuleNotFoundError or ImportError:
    from build import BoardEngine


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
