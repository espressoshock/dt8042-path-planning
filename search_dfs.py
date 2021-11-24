##############################
### SearchDFS class
##############################

# =Imports
from stack import Stack
from typing import Dict, Optional
from graph import Graph, Location
from search import Search


# Implementation following
# suggested literature
# redblob


class SearchDFS(Search):
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
    def cost_function(self, graph, from_cell, to_cell) -> float:
        return graph.cost(from_cell, to_cell)

    # ====================
    # == override ==
    # ====================
    def search(self, graph: Graph, start: Location, goal: Location) -> dict[Location, Optional[Location]]:
        frontier = Stack()
        frontier.push(start)
        came_from: dict[Location, Optional[Location]] = {}
        came_from[start] = None

        # costs
        costs: dict[Location, float] = {}
        costs[start] = 0

        while not frontier.empty():
            current: Location = frontier.pop()
            # if reached goal state, exit
            if current == goal:
                break
            for next in graph.neighbors(current):
                cost = costs[current] + \
                    self.cost_function(graph, current, next)
                if next not in came_from:
                    # compute cost
                    costs[next] = cost
                    frontier.push(next)
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
