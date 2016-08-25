# -*- coding utf-8 -*-


class Graph(object):

    def __init__(self, node_initial=None, edge_initial=None):
        '''Initialize a Grap with known Nodes and Edges
            We are expecting node_iterable, and edge_iterable to be
            lists:
                    node_initial = [n1, n2, n3....]
                    edge_initial = [(n1,n2), (n3, n1)....]
            *** If you want a graph of one node that is a list, put
                that list in a list: [[list your stuff here]]
            '''
        self.nodes = []
        self.edges = []

        if node_initial is not None:
            self.nodes = node_initial

        if edge_initial is not None:
            self.edges = edge_initial

    def nodes(self):
        '''returns a list of all nodes'''
        return self.nodes

    def edges(self):
        '''returns a list of tuples, that are edges'''
        return self.edges
