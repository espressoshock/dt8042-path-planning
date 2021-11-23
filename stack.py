##############################
### Stack Class
##############################

# =Imports
import collections

# Dequeue wrapper


class Stack:
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

    def push(self, x: any):
        self.elements.append(x)

    def pop(self) -> any:
        return self.elements.pop()
