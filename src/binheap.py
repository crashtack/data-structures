# -*- coding utf-8 -*-


# class Node(object):

    # def __init__(self, data=None, parent=None, left=None, right=None):
        # '''creating a node for a heap'''
        # self.data = data
        # self.parent = parent
        # self.left = left
        # self.right = right


class Binheap(object):

    def __init__(self, iterable=None):
        '''Initialise a heap from an iterable or an empty heap'''
        if iterable is None:
            self.heap = None
        else:
            self.heap = sorted(iterable)
        

    # def _swap(node1, node2):
        # '''returns node1 and node2 swapped'''
        # temp = node1
        # node1 = node2
        # node2 = temp
        # return node1, node2
        # pass

    def push(self, val):
        '''puts new value ito the heap, maintaining the heap property'''
        if val is None:
            raise ValueError('push requires a numeric value')
        elif self.heap is None:
            self.heap = [val]
        else:
            head = []
            tail = []
            for i, v in enumerate(self.heap):
                if v > val:
                    head = self.heap[0:i]
                    print('i am head' + head)
                    tail = self.heap[i:-1]
                    print('i am tail' + tail)
            self.heap = head
            self.heap.append(val)
            for i in tail:
                self.heap.append(i)

    def pop(self):
        '''rmoves the "top" of the heap, and resorts the heap'''
        return self.heap.pop()
