##############################
### Task 1 : Main entry Point
##############################

# =Imports
from matplotlib import pyplot as plt
import numpy as np
from search import Search
from search_bfs import SearchBFS
from simulation import Simulation
from graph import Graph, SimpleGraph, SquareGridGraph


def main():
    '''
    # TESTING

    map = Simulation.generate_2dmap([60, 60])
    bfs = SearchBFS()
    start = Simulation.extract_start_pos(map)
    goal = Simulation.extract_goal_pos(map)
    #print(map)
    sq = SquareGridGraph(len(map), len(map), map)
    bfsres = bfs.search(sq, start, goal)
    #print(sq.walls)
    #Simulation.display_plot(map)
    #print('goal: ', goal)
    #Simulation.plot_map(map, bfsres, 'Result')
    #Simulation.test()
    '''
    search = SearchBFS()

    sim = Simulation(search)
    sim.generate_random_map()
    sim.start()


if __name__ == '__main__':
    main()
