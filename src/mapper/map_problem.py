from src.data import Problem
from .map_color import MapColor
from .map_connect import MapConnect
from .map_divide import Divide
from .map_multiple import Multiple
from .split_mesh_normal import SplitMesh
from .split_mesh_2 import SplitMeshTwo
from .split_mesh_align import SplitMeshAlign


# initial map
def run_map(p: Problem, command: str) -> Problem:
    q: Problem
    # run
    if command == "identity":
        q = p.copy()
        raise DeprecationWarning
    elif command == "color":
        q = MapColor.problem(p)
    elif command == "connect":
        q = MapConnect.problem(p, True)
    elif command == "connect4":
        q = MapConnect.problem(p, False)
    elif command == "divide_row_col":
        q = Divide.problem(p)
    elif command == "multiple_row_col":
        q = Multiple.problem(p)
    elif command == "mesh_2":
        q = SplitMeshTwo.problem(p)
    elif command == "mesh_align":
        q = SplitMeshAlign.problem(p)
    elif command == "mesh_split":
        q = SplitMesh.problem(p)
    else:
        raise NotImplementedError

    return q
