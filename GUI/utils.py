import json

class Params:
    """
    Class representing parameters required to the game
    """
    def __init__(self, range: int = 6, states: int = 2, mid: bool = False, Smin: int=1, Smax: int=3, Bmin: int=2, Bmax: int=3, neighb: str="NN", sleep_time: int=1):
        """
        Args:
            range:      Range of the cells.
            states:     Number of states.
            mid:        If middle cell is included in the neighbourhood count.
            Smin:       Minimum count limit for the cell to survive.
            Smax:       Maximum count limit for the cell to survive.
            Bmin:       Minimum count limit for a dead cell to become a birth.
            Bmax:       Maximum count limit for a dead cell to become a birth.
            neighb:     Extended neighborhood type.
                        Possible values: NN - von Neumann, NM - Moore.
            sleep_time: Sleep time in seconds for changing game status.
        """
        self.range = range
        self.states = states
        self.mid = mid
        self.S = [Smin, Smax]
        self.B = [Bmin, Bmax]
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
    with open(path) as f:
        data = json.loads(f.read())
        Params.range = data["range"]
        Params.states = data["states"]
        Params.mid = data["middle"]
        Params.S = [data["Smin"], data["Smax"]]
        Params.B = [data["Bmin"], data["Bmax"]]
        Params.neighb = data["neighbourhood"]
    return params

path = "example_params.json"

#print(load_params(path).range)
#TODO: required? global OPTIONS
OPTIONS=Params()
