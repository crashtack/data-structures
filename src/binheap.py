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
        self.heap = []
        if iterable is not None:
            for i in iterable:
                self.heap.append(i)
            self.heap = self.heap.sort()


    def _swap(node1, node2):
        '''returns node1 and node2 swapped'''
        # temp = node1
        # node1 = node2
        # node2 = temp
        # return node1, node2
        pass


    def push(self, val):
        '''puts new value ito the heap, maintaining the heap property'''
        if self.heap == []:
            self.heap[0] = val
        for i in self.heap:
            if self.heap[i] > val:
                head = self.heap[0:i]
                tail = self.heap[i+1:]
        self.heap = head
        self.heap.append(val)
        for i in tail:
            self.heap.append(i)


    def pop(self):
        '''rmoves the "top" of the heap, and resorts the heap'''
        return self.heap.pop()
