##############################
### SearcAStar class
##############################

# =Imports
from priority_queue import PriorityQueue
from typing import Dict, Optional
from graph import *
from search import Search
import math
from enum import Enum

# Implementation following
# suggested literature
# redblob


class SearchAStar(Search):

    #########################
    ### Heuristics enum
    #########################
    class Heuristics(Enum):
        MANHATTAN = 0,
        EUCLIDEAN = 1,
        CUSTOM_1 = 2,
        CUSTOM_2 = 3

    #########################
    ### Constructor
    #########################
    def __init__(self, heuristic: Heuristics = Heuristics.MANHATTAN, d: float = 1):
        super().__init__()
        self._heuristic = heuristic
        self._d = d
        self._aux_info = []
        self._start = None
        pass

    # ====================
    # == override ==
    # ====================
    def __str__(self):
        base = 'SearchA*'
        if self._heuristic is self.Heuristics.EUCLIDEAN:
            base += ' [Heuristic: Euclidean]'
        elif self._heuristic is self.Heuristics.CUSTOM_1:
            base += ' [Heuristic: Custom 1]'
        elif self._heuristic is self.Heuristics.CUSTOM_2:
            base += ' [Heuristic: Custom 2]'
        else:
            base += ' [Heuristic: Manhattan]'
        return base + ' [D: '+str(self._d)+']'

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

    def _heuristic_custom1(self, a: GridLocation, b: GridLocation) -> float:
        dy_ob = abs(self._aux_info[0] - self._aux_info[1])
        mid_dy_ob = dy_ob/2

        # print('info: ', dy_ob,  mid_dy_ob, self._start[1])

        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        if self._start[1] >= mid_dy_ob:  # down
            if y1 <= mid_dy_ob:
                return 1 * (dx + dy)
            else:
                return 100 * (dx+dy)
        else:  # up
            if y1 >= mid_dy_ob:
                return 1 * (dx + dy)
            else:
                return 100 * (dx+dy)

    def heuristic(self, a: GridLocation, b: GridLocation) -> float:
        if self._heuristic is self.Heuristics.EUCLIDEAN:
            # you shouldn't be using this on a grid with 4-way movements
            return self._heuristic_euclidean(a, b)
        elif self._heuristic is self.Heuristics.CUSTOM_1:
            return self._heuristic_custom1(a, b)
        elif self._heuristic is self.Heuristics.CUSTOM_2:
            pass
        else:
            return self._heuristic_manhattan(a, b)

    # ==============
    # == override ==
    # ==============
    def cost_function(self, graph, from_cell, to_cell) -> float:
        return graph.cost(from_cell, to_cell)

    # ==============
    # == override ==
    # ==============
    def search(self, graph: Graph, start: Location, goal: Location, aux_info: list = None) -> dict[Location, Optional[Location]]:
        if aux_info != None and len(aux_info) > 0:
            self._aux_info = aux_info
            self._start = start

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
