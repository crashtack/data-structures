# -*- coding utf-8 -*-


class Node(object):

    def __init__(self, data=None, pre_node=None, next_node=None):
        self.pre_node = pre_node
        self.data = data
        self.next_node = next_node


class DoubleLinkedList(object):

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def push(self, val):
        ''' Push a node onto the head of the list '''
        new_node = Node(val)
        if self.head is None:
            print('None is None afdfda')
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre_node = new_node.data
            new_node.next_node = self.head.data
            new_node.pre_node = None
            self.head = new_node
