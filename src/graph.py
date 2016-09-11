# -*- coding utf-8 -*-
from stack import Stack
from queue_ import Queue


class Graph(object):

    def __init__(self, initial_graph=None):
        '''Pass in a graph in the form of a dictionary with the nodes as
        key, and a dictoinary containing edges as keys and wieghts as values
        {1:{2:100, 3:299},
         2:{},
         3:{1:150}}
        '''
        if initial_graph is None:
                self.graph = {}
        elif isinstance(initial_graph, dict):
            self.graph = initial_graph
        else:
            raise TypeError("Please pass a dictionary")

    def __iter__(self):
        return iter(self.graph)

    def nodes(self):
        '''return a list of all nodes in the graph'''
        # return self.depth_first_traversal(self.graph)

        return list(self.graph.keys())

    def edges(self):
        '''returns a list of tuples, that are edges'''
        return self.graph.values()

    def add_node(self, n):
        '''takes node and adds it to the graph'''
        if n in self.graph:
            raise ValueError('Node already exists please try again')
        else:
            self.graph[n] = {}

    def add_edge(self, n1, n2, w):
        '''adds a new edge to the graph connecting n1 and n2, if either
        #    n1 or n2 are not already present in the graph, they are added.'''
        # import pdb; pdb.set_trace()
        self.graph.setdefault(n2, {})
        self.graph.setdefault(n1, {})
        self.graph[n1].setdefault(n2, w)

    def del_node(self, n):
        '''deleates node n'''
        if n in self.graph.keys():
            self.graph.pop(n)
        else:
            raise ValueError('That node does not exist')

    def del_edge(self, n1, n2):
        '''deletes the edge connecting n1 and n2 from the graph,
        raises an error if no such edge exists'''
        if (n1 in self.graph) and (n2 in self.graph):
            del(self.graph[n1][n2])
        else:
            raise ValueError('That node does not exist')

    def has_node(self, n):
        '''True if node n is contained in the graph, False if not.'''
        return n in self.graph

    def neighbors(self, n):
        '''returns the list of all nodes connected to n by edges,
         raises an error if n is not in graph'''
        if n in self.graph:
            return self.graph.get(n)
        else:
            raise ValueError('That node does not exist')

    def adjacent(self, n1, n2):
        '''returns True if there is an edge connecting n1 and n2, False if not,
    raises an error if either of the supplied nodes are not in graph'''
        if (n1 in self.graph) and (n2 in self.graph):
            if n2 in self.graph[n1]:
                return True
            else:
                return False
        else:
            raise ValueError('That node does not exist')

    def _traverse(self, start, add, remove, size):
        '''Traverse function
            takes in other functions and a start_node'''
        result = []
        add(start)
        while size():
            curser = remove()
            if curser not in result:
                result.append(curser)
                for neighbor in self.graph[curser]:
                    add(neighbor)
        return result

    def depth_first_traversal(self, start_node):
        '''perform a depth first traversal, returns a list of
           nodes in the graph
        '''
        s = Stack()
        return self._traverse(start_node, s.push, s.pop, s.size)

    def breadth_first_traversal(self, start_node):
        '''perform a breadth first traversal, returns a list of
           nodes in the graph
        '''
        q = Queue()
        return self._traverse(start_node, q.enqueue, q.dequeue, q.size)


if __name__ == '__main__':
    from datetime import datetime
    g = Graph({1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7: []})

    print('\n\nRun Depth First and Breadth First Traversal\n'
          '100,000 times each on the following graph')
    message = '''
        0
      /   \\
     2      3
    / \\    / \\
   4   5  6   7
   '''
    print(message)
    now = datetime.now()
    for i in range(100000):
        result = g.depth_first_traversal(1)
    runtime = datetime.now() - now
    print('Depth First Traversal  : {} Run time: {}'.format(result, runtime))

    for i in range(100000):
        result = g.depth_first_traversal(1)
    runtime = datetime.now() - now

    print('Breadth First Traversal: {} Run time: {}'.format(result, runtime))
