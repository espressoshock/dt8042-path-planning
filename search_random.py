##############################
### SearchRandom class
##############################

# =Imports
from queue import Queue
from typing import Dict, Optional
from graph import Graph, Location
from search import Search

# Implementation following
# suggested literature
# redblob


class SearchRandom(Search):
    #########################
    ### Constructor
    #########################
    def __init__(self):
        super().__init__()
        self._prev_cost = 0
        pass

    # ====================
    # == override ==
    # ====================
    def cost_function(self, cell) -> float:
        self._prev_cost += 5
        return self._prev_cost

    # ====================
    # == override ==
    # ====================
    def search(self, graph: Graph, start: Location, goal: Location) -> dict[Location, Optional[Location]]:
        frontier = Queue()
        frontier.put(start)
        came_from: dict[Location, Optional[Location]] = {}
        came_from[start] = None

        # costs
        costs: dict[Location, float] = {}

        while not frontier.empty():
            current: Location = frontier.get_random()
            # if reached goal state, exit
            if current == goal:
                print('current', current)
                break
            for next in graph.neighbors(current):
                if next not in came_from:
                    # compute cost
                    costs[next] = self.cost_function(current)
                    frontier.put(next)
                    came_from[next] = current

        return self.extract_sssp(came_from, start, goal), costs

    # ===========
    # == Utils ==
    # ===========
    def extract_sssp(self, came_from: Dict[Location, Location], start: Location, goal: Location) -> list[Location]:
        current: Location = goal
        path: list[Location] = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # optional
        path.reverse()  # optional
        return path
