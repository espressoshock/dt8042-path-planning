##############################
### Task 1 : Main entry Point
##############################

# =Imports
from search_random import SearchRandom
from search_bfs import SearchBFS
from search_dfs import SearchDFS
from search_greedy import SearchGreedy
from search_astar import SearchAStar
from simulation import Simulation
from colorama import Fore, Back, Style, init
import random

# ===========================
# == Compound Task 1(A) ==
# ===========================


def start_task1a(n_tests: int = 3, size_base: int = 40, size_d: int = 20):
    for _ in range(n_tests):
        print(
            f'{Back.RED}{Fore.BLACK} Uninformed Search {Back.WHITE} {Style.RESET_ALL}\n')
        #random
        sim = Simulation(SearchRandom())
        size = random.randint(size_base, size_base+size_d)
        sim.generate_random_map(width=size, height=size)
        sim.start()
        #bfs
        sim.change_search(SearchBFS())
        sim.start()
        #dfs
        sim.change_search(SearchDFS())
        sim.start()
        print(
            f'\n\n{Back.RED}{Fore.BLACK} Informed Search {Back.WHITE} {Style.RESET_ALL}\n')
        #greedy
        sim.change_search(SearchGreedy())
        sim.start()
        #A* / Manhattan heuristic
        sim.change_search(SearchAStar(heuristic=SearchAStar.Heuristics.MANHATTAN))
        sim.start()
        #A* / Euclidean heuristic
        sim.change_search(SearchAStar(heuristic=SearchAStar.Heuristics.EUCLIDEAN))
        sim.start()


def main():
    init()  # init colorama
    start_task1a(n_tests=1)
    # sim = Simulation(SearchRandom())
    # sim.generate_random_map()
    # sim.start() 

    # sim = Simulation(SearchAStar(manhattan_heuristic=True, d=50))
    # sim.generate_random_map_obstacles()
    # sim.start()
    # sim.change_search(SearchAStar(manhattan_heuristic=True, d=1))
    # sim.start()



if __name__ == '__main__':
    main()
