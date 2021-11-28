##############################
### Search Class
##############################

# =Imports

class Search():
    #########################
    ### Constructor
    #########################
    def __init__(self):
        pass

    # ====================
    # == override ==
    # ====================
    def cost_function(self) -> None:
        pass

    # ====================
    # == override ==
    # ====================
    def search(self) -> None:
        pass

    # ====================
    # == override ==
    # ====================
    def __str__(self):
        return self.__class__.__name__
        pass
