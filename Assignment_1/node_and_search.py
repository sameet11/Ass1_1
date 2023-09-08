'''

Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''
from collections import deque
import queue
from time import process_time

class Node:
    '''
    This class defines nodes in search trees. It keeps track of: 
    state, cost, parent, action, and depth 
    '''
    search_cost = 0

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1 

    def goal_state(self):
        return self.state.check_goal()
    
    def successor(self, Visited_states):
        successors = queue.Queue()
        for action in self.state.action:                     
            child = self.state.move(action)
            if child != None:                              
                childNode = Node(child, self.cost + 1, self, action)
                success_string = str(child.state[0][0]) + str(child.state[0][1]) + str(child.state[1])  ###CHANGED
                if success_string not in Visited_states:   ###CHANGE
                    Visited_states.add(success_string)
                    Node.search_cost += 1
                    successors.put(childNode)
        return successors
    
    def pretty_print_solution(self, verbose):
        if self.parent is not None:
            self.parent.pretty_print_solution(verbose)
        
        print('action:', self.action)
        if verbose == True:
            self.state.pretty_print()

    def statistics_method(self, elapsed_time):
        print(f'Elapsed time (s): {elapsed_time}')
        print(f'Solution found at depth: {self.depth}')
        print(f'Number of nodes explored: {Node.search_cost}')
        print(f'Cost of solution: {self.cost}')
        print(f'Estimated effective branching factor: {Node.search_cost * (1 / self.depth)}')

class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''
    def __init__(self, problem):
        self.start = Node(problem)       
        
    def bfs(self, verbose=False, statistics=False):
        Start_time = process_time()
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        Visited_states = set()  # CHANGE
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()

            if curr_node.goal_state():
                stop = True

                if statistics:
                    Elapsed_time = process_time() - Start_time
                    curr_node.statistics_method(Elapsed_time)
                
                curr_node.pretty_print_solution(verbose)

                return curr_node    
                        
            successor = curr_node.successor(Visited_states) 
            while not successor.empty():
                success = successor.get()
                frontier.put(success)
    #using stack
    def dfs(self, verbose=False, statistics=False):
        Start_time = process_time()
        topmost = deque()
        topmost.append(self.start)
        stop = False
        Visited_states = set()  # CHANGE
        while not stop:
            if len(topmost)==0:
                return None
            curr_node = topmost.pop()

            if curr_node.goal_state():
                stop = True

                if statistics:
                    Elapsed_time = process_time() - Start_time
                    curr_node.statistics_method(Elapsed_time)
                
                curr_node.pretty_print_solution(verbose)

                return curr_node    
                        
            successor = curr_node.successor(Visited_states) 
            while not successor.empty():
                success = successor.get()
                topmost.append(success)

    #recursive
    def dfs1(self, verbose=False, statistics=False):
        def _dfs_recursive(curr_node, Visited_states):
            if curr_node.goal_state():
                if statistics:
                    Elapsed_time = process_time() - Start_time
                    curr_node.statistics_method(Elapsed_time)
                curr_node.pretty_print_solution(verbose)
                return curr_node

            successor = curr_node.successor(Visited_states)
            while not successor.empty():
                success = successor.get()
                result = _dfs_recursive(success, Visited_states)
                if result is not None:
                    return result
            return None

        Start_time = process_time()
        Visited_states = set()  # CHANGE
        curr_node = self.start
        ans = _dfs_recursive(curr_node, Visited_states)
        return ans




