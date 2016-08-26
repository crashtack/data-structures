# -*- coding utf-8 -*-


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
        print(n in self.graph.keys())
        print(self.graph.keys())

        if n in self.graph.keys():
            self.graph.pop(n)
        else:
            raise ValueError('That node does not exist')
















