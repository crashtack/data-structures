# -*- coding utf-8 -*-
from doubly_linked_list import DoubleLinkedList
from doubly_linked_list import Node


class Deque(DoubleLinkedList):

    def __init__(self, iterable=None):
        self.front = None
        self.end = None
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def peek(self):
        if self.end is None:
            return None
        else:
            return self.end.data

    def peekleft(self):
        if self.front is None:
            return None
        else:
            return self.front.data

    def size(self):
        """Returns the number of items in the list"""
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def popleft(self, arg):
        super(Deque, self).pop(arg)

    def pop(self, arg):
        super(Deque, self).shift(arg)

    def appendleft(self, arg):
        super(Deque, self).push(arg)


