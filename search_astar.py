##############################
### SearcAStar class
##############################

# =Imports
from priority_queue import PriorityQueue
from typing import Dict, Optional
from graph import *
from search import Search
import math

# Implementation following
# suggested literature
# redblob


class SearchAStar(Search):
    #########################
    ### Constructor
    #########################
    def __init__(self, manhattan_heuristic: bool = True, d: float = 1):
        super().__init__()
        self._manhattan_heuristic: bool = manhattan_heuristic
        self._d = d
        pass

    # ===============
    # == heuristic ==
    # ===============
    def _heuristic_manhattan(self, a: GridLocation, b: GridLocation) -> float:
        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return self._d * (dx+dy)

    def _heuristic_euclidean(self, a: GridLocation, b: GridLocation) -> float:
        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return self._d * math.sqrt(dx * dx + dy * dy)

    def heuristic(self, a: GridLocation, b: GridLocation) -> float:
        if self._manhattan_heuristic:
            return self._heuristic_manhattan(a, b)
        # you should be using this on a grid with 4-way movements
        return self._heuristic_euclidean(a, b)

    # ==============
    # == override ==
    # ==============
    def cost_function(self, graph, from_cell, to_cell) -> float:
        return graph.cost(from_cell, to_cell)

    # ==============
    # == override ==
    # ==============
    def search(self, graph: Graph, start: Location, goal: Location) -> dict[Location, Optional[Location]]:
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from: dict[Location, Optional[Location]] = {}
        costs: dict[Location, float] = {}
        came_from[start] = None
        costs[start] = 0

        while not frontier.empty():
            current: Location = frontier.get()
            if current == goal:
                break
            for next in graph.neighbors(current):
                cost = costs[current] + \
                    self.cost_function(graph, current, next)
                if next not in costs or cost < costs[next]:
                    costs[next] = cost
                    priority = cost + self.heuristic(next, goal)
                    frontier.put(next, priority)
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
