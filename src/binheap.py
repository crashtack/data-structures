# -*- coding utf-8 -*-


class Node(object):

    def __init__(self, data=None, parent=None, left=None, right=None):
        '''creating a node for a heap'''
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class Binheap(object):

    def __init__(self, iterable=None):
        '''Initialise a heap from an iterable or an empty heap'''
        self.top = None
        self.open = None
        self.last = None

        if iterable is not None:
            empty_list = []
            for i in iterable:
                empty_list.append(i)
            sorted_list = empty_list.sort()
            for i in sorted_list:
                self.push(i)

    def _swap(node1, node2):
        '''returns node1 and node2 swapped'''
        # temp = node1
        # node1 = node2
        # node2 = temp
        # return node1, node2
        pass


    def push():
        '''puts new node on the heap'''
