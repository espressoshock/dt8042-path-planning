##############################
### PriorityQueue classes
##############################

# =Imports
import heapq

# Implementation following
# suggested literature
# redblob


class PriorityQueue():
    #########################
    ### Constructor
    #########################
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    # ============
    # == DT fns ==
    # ============
    def empty(self) -> bool:
        return not self.elements

    def put(self, item: any, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> any:
        return heapq.heappop(self.elements)[1]
