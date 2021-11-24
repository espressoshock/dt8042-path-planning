##############################
### Queue class
##############################

# =Imports
import collections
import random

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

    def get_random(self) -> any:
        el = random.sample(self.elements, 1)[0]
        self.elements.remove(el)
        return el
