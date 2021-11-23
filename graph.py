##############################
### Graph classes
##############################

# =Imports
from typing import TypeVar, Iterator

# Implementation following
# suggested literature
# redblob
Location = TypeVar('Location')
GridLocation = tuple[int, int]


##############################
### Graph Interface
##############################
class Graph():
    #########################
    ### Constructor
    #########################
    def __init__(self):
        pass

    # ====================
    # == override ==
    # ====================
    def neighbors(self, id: Location) -> list[Location]: pass
    def cost(self, from_id: Location, to_id: Location) -> float: pass


##############################
### SimpleGraph
##############################
class SimpleGraph(Graph):
    #########################
    ### Constructor
    #########################
    def __init__(self):
        super().__init__()
        self.edges: dict[Location, list[Location]] = {}

    # ====================
    # == override ==
    # ====================
    def neighbors(self, id: Location) -> list[Location]:
        return self.edges[id]

##############################
### SquareGrid
##############################


class SquareGridGraph(Graph):
    #########################
    ### Constructor
    #########################
    def __init__(self, width: int, height: int, map: list):
        self._width = width
        self._height = height
        self._walls: list[GridLocation] = self.extract_walls(map)
        self._weights: dict[GridLocation, float] = {}

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self._width and 0 <= y < self._height

    def passable(self, id: GridLocation) -> bool:
        return id not in self._walls

    def extract_walls(self, map) -> list[GridLocation]:
        walls: list[GridLocation] = []
        for i in range(self._width):
            for j in range(self._height):
                if map[i][j] == -1:  # obstacle
                    walls.append((j, i))
        return walls

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        return self._weights.get(to_node, 1)

    # ====================
    # == override ==
    # ====================
    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        # Est, West, North, South
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        if (x + y) % 2 == 0:
            neighbors.reverse()  # Est, West, North, South
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results
