##############################
### Task 1 : Main entry Point
##############################

# =Imports
from matplotlib import colors
from search import Search
from search_random import SearchRandom
from search_bfs import SearchBFS
from search_dfs import SearchDFS
from search_greedy import SearchGreedy
from search_astar import SearchAStar
from simulation import Simulation
from colorama import Fore, Back, Style, init
import random
import matplotlib.pyplot as plt


# ===========================
# == Compound Task 1(A) ==
# ===========================


def start_task1a(n_tests: int = 3, size_base: int = 40, size_d: int = 20):
    init()  # init colorama
    for _ in range(n_tests):
        print(
            f'{Back.RED}{Fore.BLACK} Uninformed Search {Back.WHITE} {Style.RESET_ALL}\n')
        #random
        sim = Simulation(SearchRandom(), n_plots=(3, 2))  # cols, rows
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
        sim.change_search(SearchAStar(
            heuristic=SearchAStar.Heuristics.MANHATTAN))
        sim.start()
        #A* / Euclidean heuristic
        sim.change_search(SearchAStar(
            heuristic=SearchAStar.Heuristics.EUCLIDEAN))
        sim.start()
        sim.show()


def start_task1a_uninformed(n_tests: int = 3, size_base: int = 40, size_d: int = 20):
    init()  # init colorama
    for _ in range(n_tests):
        print(
            f'{Back.RED}{Fore.BLACK} Uninformed Search {Back.WHITE} {Style.RESET_ALL}\n')
        #random
        sim = Simulation(SearchRandom(), n_plots=(3, 1))  # cols, rows
        size = random.randint(size_base, size_base+size_d)
        sim.generate_random_map(width=size, height=size)
        sim.start()
        #bfs
        sim.change_search(SearchBFS())
        sim.start()
        #dfs
        sim.change_search(SearchDFS())
        sim.start()
        sim.show()


def start_task1a_informed(n_tests: int = 3, size_base: int = 40, size_d: int = 20):
    init()  # init colorama
    for _ in range(n_tests):
        print(
            f'\n\n{Back.RED}{Fore.BLACK} Informed Search {Back.WHITE} {Style.RESET_ALL}\n')
        #greedy
        sim = Simulation(SearchGreedy(), n_plots=(3, 1))  # cols, rows
        size = random.randint(size_base, size_base+size_d)
        sim.generate_random_map(width=size, height=size)
        sim.start()
        #A* / Manhattan heuristic
        sim.change_search(SearchAStar(
            heuristic=SearchAStar.Heuristics.MANHATTAN))
        sim.start()
        #A* / Euclidean heuristic
        sim.change_search(SearchAStar(
            heuristic=SearchAStar.Heuristics.EUCLIDEAN))
        sim.start()
        sim.show()


def start_task1b_point2(size_base: int = 40, size_d: int = 20):
    sim = Simulation(SearchRandom(), n_plots=(3, 2))
    size = random.randint(size_base, size_base+size_d)
    sim.generate_random_map_obstacles(size, size)
    sim.start()
    sim.change_search(SearchBFS())
    sim.start()
    sim.change_search(SearchDFS())
    sim.start()
    sim.change_search(SearchGreedy())
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.EUCLIDEAN, d=1))
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.MANHATTAN, d=1))
    sim.start()
    sim.show()


def start_task1b_point3():
    sim = Simulation(SearchAStar(
        heuristic=SearchAStar.Heuristics.MANHATTAN, d=1), n_plots=(2, 2))
    sim.generate_random_map_obstacles()
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.EUCLIDEAN, d=1))
    sim.start()
    # sim.change_search(SearchAStar(
    #     heuristic=SearchAStar.Heuristics.MANHATTAN, d=100))
    # sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.CUSTOM_1, d=1))
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.CUSTOM_2, d=1))
    sim.start()
    sim.show()


def start_task1b_point3_bonus():
    sim = Simulation(SearchAStar(
        heuristic=SearchAStar.Heuristics.MANHATTAN, d=1), n_plots=(3, 2))
    sim.generate_random_map_obstacles()
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.MANHATTAN, d=100))
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.CUSTOM_1, d=1))
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.CUSTOM_2, d=1))
    sim.start()
    sim.change_search(SearchAStar(
        heuristic=SearchAStar.Heuristics.CUSTOM_3, d=1))
    sim.start()
    sim.show(True)


def start_statistical_comparison(n_tests: int = 3, size_base: int = 40, size_d: int = 20, plot_map: bool = False):
    def _gen_data(n_tests, size_base, size_d, plot_map):
        s_data = {'random': [], 'bfs': [], 'dfs': [], 'greedy': [], 'a_mh_1': [
        ], 'a_eh_1': [], 'a_ch1': [], 'a_ch2': [], 'a_ch3': [], 'a_mh_100': []}
        for _ in range(n_tests):
            #random
            sim = Simulation(SearchRandom(), n_plots=(5, 2))  # cols, rows
            size = random.randint(size_base, size_base+size_d)
            print(f'Map Size: w:{size}, h:{size}')
            sim.generate_random_map_obstacles(width=size, height=size)
            s_data['random'].append(sim.start(generate_stats=False))
            #bfs
            sim.change_search(SearchBFS())
            s_data['bfs'].append(sim.start(generate_stats=False))
            #dfs
            sim.change_search(SearchDFS())
            s_data['dfs'].append(sim.start(generate_stats=False))
            #greedy
            sim.change_search(SearchGreedy())
            s_data['greedy'].append(sim.start(generate_stats=False))
            #A* / Manhattan heuristic
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.MANHATTAN, d=1))
            s_data['a_mh_1'].append(sim.start(generate_stats=False))
            #A* / Euclidean heuristic
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.EUCLIDEAN, d=1))
            s_data['a_eh_1'].append(sim.start(generate_stats=False))
            #A* / Custom heuristic 1
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.CUSTOM_1, d=1))
            s_data['a_ch1'].append(sim.start(generate_stats=False))
            #A* / Custom heuristic 2
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.CUSTOM_2, d=1))
            s_data['a_ch2'].append(sim.start(generate_stats=False))
            #A* / Custom heuristic 3
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.CUSTOM_3, d=1))
            s_data['a_ch3'].append(sim.start(generate_stats=False))
            #A* / Custom precomputed exact heuristic
            sim.change_search(SearchAStar(
                heuristic=SearchAStar.Heuristics.MANHATTAN, d=100))
            s_data['a_mh_100'].append(sim.start(generate_stats=False))
        #optionally show plot
        if plot_map:
            sim.show()
        return s_data, (sim._start, sim._goal)

    def aggreate_res(data):
        ne_data = {'random': [], 'bfs': [], 'dfs': [], 'greedy': [], 'a_mh_1': [
        ], 'a_eh_1': [], 'a_ch1': [], 'a_ch2': [], 'a_ch3': [], 'a_mh_100': []}
        sp_data = {'random': [], 'bfs': [], 'dfs': [], 'greedy': [], 'a_mh_1': [
        ], 'a_eh_1': [], 'a_ch1': [], 'a_ch2': [], 'a_ch3': [], 'a_mh_100': []}
        for key in data:
            for i in data[key]:
                ne_data[key].append(len(i[1]))  # expanded nodes
                sp_data[key].append(len(i[0]))  # path length
                # cost not used as costs = len(path)+1, where p_cost = 1
        return ne_data, sp_data

    def mean(data):
        res = []
        for cl in data:
            i = 0
            m = 0
            for v in cl:
                m += v
                i += 1
            res.append(m/i)
        return res

    data, _sim = _gen_data(n_tests, size_base, size_d, plot_map)
    ne_data, sp_data = aggreate_res(data)
    plt.close('all')
    plt.clf()
    # plt.figure(2)
    # 'transpose' items to parallel key, value lists
    labels, ne_values = [*zip(*ne_data.items())]
    # 'transpose' items to parallel key, value lists
    labels, sp_values = [*zip(*sp_data.items())]

    gh_colors = ['#332288', '#117733', '#44AA99', '#88CCEE',
                 '#DDCC77', '#CC6677', '#AA4499', '#882255']

    print('\n\n\ncomp: ', ne_values)
    print('\n\n\ncomp: ', sp_values)

    # ne
    plt.clf()
    plt.boxplot(ne_values)
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.title('Box plot of Nodes expanded by Algorithms/Heuristic')
    plt.show()

    #sp
    plt.clf()
    plt.boxplot(sp_values)
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.title('Box plot of path length by Algorithms/Heuristic')
    plt.show()

    # mean nodes expanded
    plt.clf()
    plt.bar(labels, mean(ne_values), color=gh_colors)
    plt.title('Mean of Nodes expanded by algorithm/heuristic')
    plt.show()

    # mean path
    plt.clf()
    plt.bar(labels, mean(sp_values), color=gh_colors)
    plt.title('Mean of path length by algorithm/heuristic')
    plt.show()


def main():
    # ================
    # == Start here ==
    # ================
    # uncomment below
    # ================
    start_task1a(n_tests=1)
    # start_task1b_point2(60, 0)
    # start_task1b_point3()
    # start_task1b_point3_bonus()  # bonus with pre-computed exact path
    # start_statistical_comparison(n_tests=20, size_base=60, size_d=0, plot_map=False)

    #for comparison / report
    # start_task1a_uninformed(n_tests=1)
    # start_task1a_informed(n_tests=1)


if __name__ == '__main__':
    main()
