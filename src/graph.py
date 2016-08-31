# -*- coding utf-8 -*-
from stack import Stack

class Graph(object):

    def __init__(self, initial_graph=None):
        '''Pass in a graph in the form of a dictionary with the nodes as
        key, and a list of edges as value, for example
        {1:[2, 3]},
         2:[]},
         3:[1]}
        '''
        if initial_graph is None:
            self.graph = {}
        else:
            self.graph = initial_graph

    def __iter__(self):
        return iter(self.graph)

    def nodes(self):
        '''return a list of all nodes in the graph'''
        return self.graph.keys()

    def edges(self):
        '''returns a list of tuples, that are edges'''
        return self.graph.values()

    def add_node(self, n):
        '''takes node and adds it to the graph'''
        if n in self.graph:
            raise ValueError('Node already exists please try again')
        else:
            self.graph[n] = []

    def add_edge(self, n1, n2):
        '''adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already
         present in the graph, they are added.'''
        if n2 not in self.graph:
            self.graph[n2] = []
        if n1 in self.graph:
            self.graph[n1].append(n2)
        else:
            self.graph[n1] = [n2]

    def del_node(self, n):
        if n in self.graph.keys():
            self.graph.pop(n)
        else:
            raise ValueError('That node does not exist')

    def del_edge(self, n1, n2):
        '''deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
        raises an error if no such edge exists'''
        if (n1 in self.graph) and (n2 in self.graph):
            self.graph[n1].remove(n2)
        else:
            raise ValueError('That node does not exist')

    def has_node(self, n):
        '''True if node ‘n’ is contained in the graph, False if not.'''
        return n in self.graph

    def neighbors(self, n):
        '''returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in graph'''
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
        s = Stack()
        s.add(start)
        while s.size():
            curser = s.remove()
            if curser not in result:
                result.append(curser)
                for neighbor in curser:
                    s.add(neighbor)
        return result



    def depth_first_traversal(self, start_node):
        '''perform a depth first traversal, returns a list of
           nodes in the graph
        '''

        return _traverse(start_node, Stack.push(), Stack.pop(), Stack.size())








# a comment at the bottom of the page
