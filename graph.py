##############################
### Graph classes
##############################

# =Imports
from typing import TypeVar

# Implementation following
# suggested literature
# redblob
Location = TypeVar('Location')


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
    pass


##############################
### Graph Interface
##############################
class SimpleGraph(Graph):
    #########################
    ### Constructor
    #########################
    def __init__(self):
        super().__init__()
        self.edges: Dict[Location, list[Location]] = {}

    # ====================
    # == override ==
    # ====================
    def neighbors(self, id: Location) -> list[Location]:
        return self.edges[id]
