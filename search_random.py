##############################
# SearchRandom class
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
    # Constructor
    #########################
    def __init__(self):
        super().__init__()
        self._prev_cost = 0
        pass

    # ====================
    # == override ==
    # ====================
    def __str__(self):
        return self.__class__.__name__

    # ====================
    # == override ==
    # ====================
    def cost_function(self, graph, from_cell, to_cell) -> float:
        return graph.cost(from_cell, to_cell)

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
        costs[start] = 0

        while not frontier.empty():
            current: Location = frontier.get_random()
            # if reached goal state, exit
            if current == goal:
                break
            for next in graph.neighbors(current):
                cost = costs[current] + \
                    self.cost_function(graph, current, next)
                if next not in came_from:
                    # compute cost
                    costs[next] = cost
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
