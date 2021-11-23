##############################
### Queue class
##############################

# =Imports
import collections

# Implementation following
# suggested literature
# redblob

# Dequeue wrapper


class Queue:
    #########################
    ### Constructor
    #########################
    def __init__(self):
        self.elements = collections.deque()

    # ============
    # == DT fns ==
    # ============
    def empty(self) -> bool:
        return not self.elements

    def put(self, x: any):
        self.elements.append(x)

    def get(self) -> any:
        return self.elements.popleft()
