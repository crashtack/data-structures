class Node(object):

    def __init__(self, edges={}):
        self.edges = edges
        self.distance = float('inf')
        self.visited = False

    def get_edges(self):
        return self.edges.keys()

    def get_weight(self, neighbor):
        return self.edges[neighbor]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_visited(self):
        self.vistited = True


class Graph(object):

    def __init__(self, initial_graph=None):
        '''Pass in a graph in the form of a dictionary with the nodes as
        key, and a dictoinary containing edges as keys and wieghts as values
        {1:{2:100, 3:299},
         2:{},
         3:{1:150}}
        '''
        self.nodes = {}
        if initial_graph is not None:
            for k in initial_graph.keys():
                self.nodes.setdefault(k, Node(initial_graph[k]))

    def add_nodes(self, id_, edges):
        self.nodes.setdefault(id_, edges)






#
