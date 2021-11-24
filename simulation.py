##############################
### Simulation class
##############################

# =Imports
import numpy as np
import matplotlib.pyplot as plt
from graph import SquareGridGraph
from search import Search
from search_bfs import SearchBFS
from colorama import Fore, Back, Style, init


class Simulation():
    #########################
    ### SIM-CONSTANTS
    #########################
    OBSTACLE_DENSITY = 0.9

    #########################
    ### Constructor
    #########################
    def __init__(self, search: Search = SearchBFS):
        self._2dmap: list = []
        self._2dmap_solved: list = []
        self._search: Search = search
        self._graph: SquareGridGraph = None
        self._start = None
        self._goal = None
        init()  # init colorama

    ##############################
    ### Task 1 / Random Obstacles
    ##############################

    # =====================
    # == 0. Generate Map ==
    # =====================
    def generate_random_map(self, width: int = 60, height: int = 60):
        self._2dmap = Simulation.generate_2dmap([width, height])
        self.generate_grid_graph(width, height, self._2dmap)
        self.extract_start_goal(self._2dmap)

    # ===========================
    # == 1. Generate GridGraph ==
    # ===========================
    def generate_grid_graph(self, width: int, height: int, map: list):
        self._graph = SquareGridGraph(width, height, map)

    # ===========================
    # == 2. Extract start/goal ==
    # ===========================
    def extract_start_goal(self, map: list):
        self._start, self._goal = Simulation.extract_start_pos(
            map), Simulation.extract_goal_pos(map)

    # ==============================
    # == 3. Extract expanded node ==
    # ==============================

    def merge_expanded_nodes(self, cost_map: dict):
        self._2dmap_solved = self._2dmap[:]
        for cx in cost_map.keys():
            if cx != self._start and cx != self._goal and cx != (0, 0):
                x, y = cx[0], cx[1]
                self._2dmap_solved[y][x] = cost_map[cx]
        print('final map', self._2dmap[0:5])

    # ============================
    # == 4. Generate Statistics ==
    # ============================
    def generate_statistics(self, path: list, costs: list, output: bool = False):
        if output:
            print(f'{Back.YELLOW}{Fore.BLACK} Statistics {Back.WHITE}{Fore.BLACK} {self._search.__class__.__name__} {Style.RESET_ALL}')
            print(
                f'{" "*2}{Back.CYAN} Nodes expanded {Back.GREEN} {Fore.BLACK}{len(costs)} {Style.RESET_ALL}')
            print(
                f'{" "*2}{Back.BLUE} Path length {Back.GREEN}{Fore.BLACK} {len(path)} {Style.RESET_ALL}')
            print(
                f'{" "*2}{Back.MAGENTA} Path cost {Back.GREEN} {Fore.BLACK}{costs[self._goal]} {Style.RESET_ALL}')
        #nodes opened, path length and path cost
        return (len(costs), len(path), costs[self._goal])

    # =======================
    # == 4. Perform search ==
    # =======================

    def start(self):
        path, costs = self._search.search(self._graph, self._start, self._goal)
        self.generate_statistics(path, costs, True)
        self.merge_expanded_nodes(costs)
        Simulation.plot_map(self._2dmap_solved, path, '' +
                            self._search.__class__.__name__)

    #########################
    ### Built-in Test
    #########################

    #goes through built-in provided sample

    @staticmethod
    def test():
        # create a map with obstacles randomly distributed
        #  0 - Free cell
        # -1 - Obstacle
        # -2 - Start point
        # -3 - Goal point
        _map_ = Simulation.generate_2dmap([60, 60])
        plt.clf()
        plt.imshow(_map_)
        plt.show()

        # map with rotated-H shape obstacle and obstacles randomly distributed
        map_h_object, info = Simulation.generate_2dmap_obstacles([60, 60])

        # environment information
        print("map info: ")
        print("y top: ", info[0])
        print("t bot: ", info[1])
        print("x wall: ", info[2])

        plt.clf()
        plt.imshow(map_h_object)
        plt.show()

        # example for a solved_map
        #  0 - unexpanded cell
        # -1 - obstacle
        # -2 - start point
        # -3 - goal point
        # positive_numbers - one type of the values described in lab2 description (heuristic cost, travel cost, cell total cost,...)

        example_solved_map = map_h_object
        example_solved_path = np.array(
            [[xx, xx*2] if xx % 2 == 0 else [xx, xx+1] for xx in range(20)])

        print("path", example_solved_path)

        Simulation.plot_map(example_solved_map, example_solved_path)

    #########################
    ### Helpers / Provided
    #########################

    # ========================
    # == Feature extraction ==
    # ========================
    @staticmethod
    def extract_start_pos(map: list) -> tuple[int, int]:
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == -2:  # obstacle
                    return (j, i)
        return (0, 0)

    @staticmethod
    def extract_goal_pos(map: list) -> tuple[int, int]:
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == -3:  # obstacle
                    return (j, i)
        return (0, 0)

    # ====================
    # == Map Generation ==
    # ====================

    @staticmethod
    def generate_2dmap(size_):
        '''Generates a random 2d map with obstacles (small blocks) randomly distributed. 
        You can specify any size of this map but your solution has to be independent of map size

        Parameters:
        -----------
        size_ : list
            Width and height of the 2d grid map, e.g. [60, 60]. The height and width of the map shall be greater than 20.

        Returns:
        --------
            map2d : array-like, shape (size_[0], size_[1])
            A 2d grid map, cells with a value of 0: Free cell; 
                                                    -1: Obstacle;
                                                    -2: Start point;
                                                    -3: Goal point;
        '''

        size_x, size_y = size_[0], size_[1]

        map2d = np.random.rand(size_y, size_x)
        perObstacles_ = Simulation.OBSTACLE_DENSITY
        map2d[map2d <= perObstacles_] = 0
        map2d[map2d > perObstacles_] = -1

        yloc, xloc = [np.random.random_integers(
            0, size_x-1, 2), np.random.random_integers(0, size_y-1, 2)]
        while (yloc[0] == yloc[1]) and (xloc[0] == xloc[1]):
            yloc, xloc = [np.random.random_integers(
                0, size_x-1, 2), np.random.random_integers(0, size_y-1, 2)]

        map2d[xloc[0]][yloc[0]] = -2
        map2d[xloc[1]][yloc[1]] = -3

        return map2d

    # Generate 2d grid map with rotated-H-shape object
    @staticmethod
    def generate_2dmap_obstacles(size_):
        '''Generates a random 2d map with a rotated-H-shape object in the middle and obstacles (small blocks) randomly distributed. 
        You can specify any size of this map but your solution has to be independent of map size

        Parameters:
        -----------
        size_ : list
            Width and height of the 2d grid map, e.g. [60, 60]. The height and width of the map shall be greater than 40.

        Returns:
        --------
            map2d : array-like, shape (size_[0], size_[1])
            A 2d grid map, cells with a value of 0: Free cell; 
                                                -1: Obstacle;
                                                -2: Start point;
                                                -3: Goal point;
                                                
        [ytop, ybot, minx] : list
            information of the rotated-H-shape object
            ytop - y coordinate of the top horizontal wall/part
            ybot - y coordinate of the bottom horizontal wall/part
            minx - X coordinate of the vertical wall 
        '''

        size_x, size_y = size_[0], size_[1]
        map2d = Simulation.generate_2dmap(size_)

        map2d[map2d == -2] = 0
        map2d[map2d == -3] = 0

        # add special obstacle
        xtop = [np.random.random_integers(
            5, 3*size_x//10-2), np.random.random_integers(7*size_x//10+3, size_x-5)]
        ytop = np.random.random_integers(7*size_y//10 + 3, size_y - 5)
        xbot = np.random.random_integers(
            3, 3*size_x//10-5), np.random.random_integers(7*size_x//10+3, size_x-5)
        ybot = np.random.random_integers(5, size_y//5 - 3)

        map2d[ybot, xbot[0]:xbot[1]+1] = -1
        map2d[ytop, xtop[0]:xtop[1]+1] = -1
        minx = (xbot[0]+xbot[1])//2
        maxx = (xtop[0]+xtop[1])//2
        if minx > maxx:
            tempx = minx
            minx = maxx
            maxx = tempx
        if maxx == minx:
            maxx = maxx+1

        map2d[ybot:ytop, minx:maxx] = -1
        startp = [np.random.random_integers(
            0, size_x//2 - 4), np.random.random_integers(ybot+1, ytop-1)]

        map2d[startp[1], startp[0]] = -2
        goalp = [np.random.random_integers(
            size_x//2 + 4, size_x - 3), np.random.random_integers(ybot+1, ytop-1)]

        map2d[goalp[1], goalp[0]] = -3
        #return map2d, [startp[1], startp[0]], [goalp[1], goalp[0]], [ytop, ybot]
        return map2d, [ytop, ybot, minx]

    # ====================
    # == Map Plotting ==
    # ====================
    @staticmethod
    def display_plot(plot):
        plt.clf()
        plt.imshow(plot)
        plt.show()

    # helper function for plotting the result
    @staticmethod
    def plot_map(map2d_, path_, title_=''):
        '''Plots a map (image) of a 2d matrix with a path from start point to the goal point. 
            cells with a value of 0: Free cell; 
                                -1: Obstacle;
                                -2: Start point;
                                -3: Goal point;
        Parameters:
        -----------
        map2d_ : array-like
            an array with Real Numbers
            
        path_ : array-like
            an array of 2d corrdinates (of the path) in the format of [[x0, y0], [x1, y1], [x2, y2], ..., [x_end, y_end]]
            
        title_ : string
            information/description of the plot

        Returns:
        --------

        '''

        import matplotlib.cm as cm
        plt.interactive(False)

        colors_nn = int(map2d_.max())
        colors = cm.winter(np.linspace(0, 1, colors_nn))

        colorsMap2d = [[[] for x in range(map2d_.shape[1])]
                       for y in range(map2d_.shape[0])]
        # Assign RGB Val for starting point and ending point
        locStart, locEnd = np.where(map2d_ == -2), np.where(map2d_ == -3)

        colorsMap2d[locStart[0][0]][locStart[1]
                                    [0]] = [.0, 1, .0, 1.0]  # green
        colorsMap2d[locEnd[0][0]][locEnd[1][0]] = [1.0, .7, .27, 1.0]  # yellow

        # Assign RGB Val for obstacle
        locObstacle = np.where(map2d_ == -1)
        for iposObstacle in range(len(locObstacle[0])):
            colorsMap2d[locObstacle[0][iposObstacle]
                        ][locObstacle[1][iposObstacle]] = [1.0, .0, .0, 1.0]  # red
        # Assign 0
        locZero = np.where(map2d_ == 0)

        for iposZero in range(len(locZero[0])):
            colorsMap2d[locZero[0][iposZero]][locZero[1]
                                              [iposZero]] = [1.0, 1.0, 1.0, 1.0]

        # Assign Expanded nodes
        locExpand = np.where(map2d_ > 0)

        for iposExpand in range(len(locExpand[0])):
            _idx_ = int(map2d_[locExpand[0][iposExpand]]
                        [locExpand[1][iposExpand]]-1)
            colorsMap2d[locExpand[0][iposExpand]
                        ][locExpand[1][iposExpand]] = colors[_idx_]

        for irow in range(len(colorsMap2d)):
            for icol in range(len(colorsMap2d[irow])):
                if colorsMap2d[irow][icol] == []:
                    colorsMap2d[irow][icol] = [1.0, 0.0, 0.0, 1.0]

        print('path: ', path_)
        path = np.array(list(path_)).T.tolist()

        plt.figure()
        plt.title(title_)
        plt.imshow(colorsMap2d, interpolation='nearest')
        plt.colorbar()
        plt.plot(path[:][0], path[:][1], color='magenta', linewidth=2.5)
        plt.show()
