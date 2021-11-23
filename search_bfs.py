##############################
### SearchBFS class
##############################

# =Imports
from queue import Queue
from typing import Dict, Optional
from graph import Graph, Location
from search import Search

# Implementation following
# suggested literature
# redblob


class SearchBFS(Search):
    #########################
    ### Constructor
    #########################
    def __init__(self):
        super().__init__()
        pass

    # ====================
    # == override ==
    # ====================
    def search(self, graph: Graph, start: Location, goal: Location) -> dict[Location, Optional[Location]]:
        frontier = Queue()
        frontier.put(start)
        came_from: dict[Location, Optional[Location]] = {}
        came_from[start] = None

        while not frontier.empty():
            current: Location = frontier.get()
            # if reached goal state, exit
            if current == goal:
                print('current', current)
                break
            for next in graph.neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current

        return self.extract_sssp(came_from, start, goal)

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

