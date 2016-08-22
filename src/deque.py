# -*- coding utf-8 -*-
from doubly_linked_list import DoubleLinkedList
from doubly_linked_list import Node


class Deque(DoubleLinkedList):

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable is not None:
            for i in iterable:
                self.appendleft(i)

    def peek(self):
        if self.tail is None:
            return None
        else:
            return self.tail.data

    def peekleft(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def size(self):
        """Returns the number of items in the list"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def popleft(self):
        super(Deque, self).pop()

    def pop(self):
        return super(Deque, self).shift()

    def appendleft(self, arg):
        super(Deque, self).push(arg)
