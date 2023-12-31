'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals 
from node_and_search import SearchAlgorithm

init_state = [[0, 0], 'r', [3, 3]] 
goal_state = [[3, 3], 'l', [0, 0]] 

def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs()
    print('goal state: ')
    goal_node.state.pretty_print()

    
    solution = sa.bfs(verbose=True)
    solution = sa.bfs(statistics=True)
if __name__ == "__main__":
    main()