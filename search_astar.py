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
from numpy import interp

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
        CUSTOM_2 = 3,
        CUSTOM_3 = 4

    #########################
    ### Constructor
    #########################
    def __init__(self, heuristic: Heuristics = Heuristics.MANHATTAN, d: float = 1):
        super().__init__()
        self._heuristic = heuristic
        self._d = d
        self._aux_info = []
        self._start = None
        self._goal = None
        pass

    # ====================
    # == override ==
    # ====================
    def __str__(self):
        base = 'SearchA*'
        if self._heuristic is self.Heuristics.EUCLIDEAN:
            base += ' [Heuristic: Euclidean]'+' [D: '+str(self._d)+']'
        elif self._heuristic is self.Heuristics.CUSTOM_1:
            base += ' [Heuristic: Custom 1]'
        elif self._heuristic is self.Heuristics.CUSTOM_2:
            base += ' [Heuristic: Custom 2]'
        elif self._heuristic is self.Heuristics.CUSTOM_3:
            base += ' [Heuristic: Custom 3]'
        else:
            base += ' [Heuristic: Manhattan]' + ' [D: '+str(self._d)+']'
        return base

    # ================
    # == heuristics ==
    # ================
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

        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        #don't overestimate, worst underestimate

        if x1 < self._aux_info[2]:  # left
            if self._start[1] > mid_dy_ob:  # downward
                dy_end_obs = abs(self._aux_info[1]-y1)
                dx_flip = abs(x1 - x2)
                dy_end_goal = abs(y2 - self._aux_info[1])
                return dy_end_obs + dx_flip + dy_end_goal
            else:  # upward
                dy_end_obs = abs(self._aux_info[0]-y1)
                dx_flip = abs(x1 - x2)
                dy_end_goal = abs(y2 - self._aux_info[0])
                return dy_end_obs + dx_flip + dy_end_goal
        else:  # right
            return 1 * (dx + dy)

    def _heuristic_custom2(self, a: GridLocation, b: GridLocation) -> float:
        dy_ob = abs(self._aux_info[0] - self._aux_info[1])
        mid_dy_ob = dy_ob/2

        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        overestimate_correction = 0

        if y1 > self._aux_info[0] and y1 < self._aux_info[1]:  # within
            #decide direction
            if self._start[1] >= mid_dy_ob:  # down
                dy_end_trg = abs(
                    self._aux_info[1]-y1)
                return (dy_end_trg - overestimate_correction) * (dx+dy)
            else:  # up
                dy_end_trg = abs(
                    self._aux_info[1]-y1)
                return (dy_end_trg - overestimate_correction) * (dx+dy)
        else:  # overshoot go right
            if x1 < self._goal[0]:
                dx_end_trg = abs(
                    self._goal[0]-x1)
                return (dx_end_trg - overestimate_correction) * (dx+dy)
            else:  # overshoot to the right, go down
                if self._goal[1] >= y1:  # down
                    dy_end_trg = abs(
                        self._goal[1]-y1)
                    return (dy_end_trg - overestimate_correction) * (dx+dy)
                else:  # up
                    dy_end_trg = abs(
                        self._goal[1]-y1)
                    return (dy_end_trg - overestimate_correction) * (dx+dy)

    def _heuristic_custom3(self, a: GridLocation, b: GridLocation) -> float:
        dy_ob = abs(self._aux_info[0] - self._aux_info[1])
        mid_dy_ob = dy_ob/2

        # print('info: ', dy_ob,  mid_dy_ob, self._start[1])

        (x1, y1) = a
        (x2, y2) = b  # goal
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        overestimate_correction = 0
        exact_heuristic = [1, 5]

        if y1 > self._aux_info[0] and y1 < self._aux_info[1]:  # within
            #decide direction
            if self._start[1] >= mid_dy_ob:  # down
                dy_end_trg = abs(
                    self._aux_info[1]-y1)
                return (interp(dy_end_trg, [0, dy_ob], exact_heuristic) - overestimate_correction) * (dx+dy)
            else:  # up
                dy_end_trg = abs(
                    self._aux_info[1]-y1)
                return (interp(dy_end_trg, [0, dy_ob], exact_heuristic) - overestimate_correction) * (dx+dy)
        else:  # overshoot go right
            if x1 < self._goal[0]:
                dx_end_trg = abs(
                    self._goal[0]-x1)
                return (interp(dx_end_trg, [0, dy_ob], exact_heuristic) - overestimate_correction) * (dx+dy)
            else:  # overshoot to the right, go down
                if self._goal[1] >= y1:  # down
                    dy_end_trg = abs(
                        self._goal[1]-y1)
                    return (interp(dy_end_trg, [0, dy_ob], exact_heuristic) - overestimate_correction) * (dx+dy)
                else:  # up
                    dy_end_trg = abs(
                        self._goal[1]-y1)
                    return (interp(dy_end_trg, [0, dy_ob], exact_heuristic) - overestimate_correction) * (dx+dy)

    def heuristic(self, a: GridLocation, b: GridLocation) -> float:
        if self._heuristic is self.Heuristics.EUCLIDEAN:
            # you shouldn't be using this on a grid with 4-way movements
            return self._heuristic_euclidean(a, b)
        elif self._heuristic is self.Heuristics.CUSTOM_1:
            return self._heuristic_custom1(a, b)
        elif self._heuristic is self.Heuristics.CUSTOM_2:
            return self._heuristic_custom2(a, b)
        elif self._heuristic is self.Heuristics.CUSTOM_3:
            return self._heuristic_custom3(a, b)
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
            self._goal = goal

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
