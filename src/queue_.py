# -*- coding utf-8 -*-


class Node(object):

    def __init__(self, data=None, pre_node=None, next_node=None):
        self.pre_node = pre_node
        self.data = data
        self.next_node = next_node


class Queue(object):
    def __init__(self, iterable=None):
        self.front = None
        self.back = None
        if iterable is not None:
            for i in iterable:
                self.enqueue(i)

    def enqueue(self, val):
        new_node = Node(val)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.pre_node = new_node
            new_node.next_node = self.back
            new_node.pre_node = None
            self.back = new_node

    def dequeue(self):
        try:
            returned_value = self.front.data
        except AttributeError:
            raise IndexError('Can not remove from empty queue.')
        self.front = self.front.pre_node
        try:
            self.front.next_node = None
        except AttributeError:
            pass
        return returned_value

    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data

    def size(self):
        if self.front is None:
            return 0
