import pytest
from GUI.board_display import BoardWindow
try:
    from build.Debug import generatedBoardEngineModuleName
except ModuleNotFoundError or ImportError:
    from build import generatedBoardEngineModuleName


def test_pybind():
    """
    Tests whether connection with C++ module works and checks if returned gameboard's type is correct.
    """
    game_engine = generatedBoardEngineModuleName.PySomeClass()
    gameboard = game_engine.get_board()
    assert isinstance(gameboard, list)
