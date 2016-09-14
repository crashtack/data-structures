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


    def dijkstra(self, start, finish):
        '''returns the shortest path from start to finish node'''
        visited = {self.nodes[start]}
        not_visited = False

        return []

#
