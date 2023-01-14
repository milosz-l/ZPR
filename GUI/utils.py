"""
    Module responsible for a class with game's parameters.
"""

import json


class Params:  # pylint: disable=too-few-public-methods
    """
    Class representing parameters required to the game
    """

    def __init__(
        self,
        range: int = 1,
        states: int = 2,
        mid: bool = False,
        s_min: int = 2,
        s_max: int = 3,
        b_min: int = 3,
        b_max: int = 3,
        neighb: str = "NM",
        sleep_time: int = 1,
    ):  # pylint: disable=too-many-arguments,redefined-builtin
        """
        Args:
            range:      Range of the cells.
            states:     Number of states.
            mid:        If middle cell is included in the neighbourhood count.
            s_min:      Minimum count limit for the cell to survive.
            s_max:      Maximum count limit for the cell to survive.
            b_min:      Minimum count limit for a dead cell to become a birth.
            b_max:      Maximum count limit for a dead cell to become a birth.
            neighb:     Extended neighborhood type.
                        Possible values: NN - von Neumann, NM - Moore.
            sleep_time: Sleep time in seconds for changing game status.
        """
        self.range = range
        self.states = states
        self.mid = mid
        self.s_range = [s_min, s_max]
        self.b_range = [b_min, b_max]
        self.neighb = neighb
        self.sleep_time = sleep_time


def load_params(path: str) -> Params:
    """
    Loading parameters from a json file.

    Args:
        path:       Path to the json file with parameters.

    Returns:
        Object of type Params with parameters extracted from the file.
    """
    params = Params()
    with open(path, encoding="utf-8") as file:
        data = json.loads(file.read())
        Params.range = data["range"]
        Params.states = data["states"]
        Params.mid = data["middle"]
        Params.s_range = [data["s_min"], data["s_max"]]
        Params.b_range = [data["b_min"], data["b_max"]]
        Params.neighb = data["neighbourhood"]
    return params


OPTIONS = Params()
