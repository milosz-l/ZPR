import json

class Params:
    def __init__(self, range: int = 6, states: int = 2, mid: bool = False, Smin=1, Smax=3, Bmin=2, Bmax=3, neighb="NN"):
        self.range = range
        self.states = states
        self.mid = mid
        self.S = [Smin, Smax]
        self.B = [Bmin, Bmax]
        self.neighb = neighb

def load_params(path):
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
