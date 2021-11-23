##############################
### SearchGreedy class
##############################

# =Imports
from priority_queue import PriorityQueue
from typing import Dict, Optional
from graph import Graph, Location
from search import Search

# Implementation following
# suggested literature
# redblob


class SearchGreedy(Search):
    #########################
    ### Constructor
    #########################
    def __init__(self):
        super().__init__()
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
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from: Dict[Location, Optional[Location]] = {}
        costs: Dict[Location, float] = {}
        came_from[start] = None
        costs[start] = 0
        
        while not frontier.empty():
            current: Location = frontier.get()
            
            if current == goal:
                break
            
            for next in graph.neighbors(current):
                cost = costs[current] + self.cost_function(graph, current, next)
                if next not in costs or cost < costs[next]:
                    costs[next] = cost
                    priority = cost
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
        path.append(start) # optional
        path.reverse() # optional
        return path