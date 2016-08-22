# -*- coding utf-8 -*-
from doubly_linked_list import DoubleLinkedList


class Deque(DoubleLinkedList):

    def __init__(self, iterable=None):
        '''Initialises an empty deque or a deque made from a passed in iterable'''
        self.head = None
        self.tail = None
        if iterable is not None:
            for i in iterable:
                self.appendleft(i)

    def peek(self):
        '''returns the next value that would be returned by pop but leaves the value in the deque'''
        if self.tail is None:
            return None
        else:
            return self.tail.data

    def peekleft(self):
        '''returns the next value that would be returned by popleft but leaves the value in the deque'''
        if self.head is None:
            return None
        else:
            return self.head.data

    def size(self):
        '''Returns the number of items in the list'''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def popleft(self):
        '''removes a value from the front of the deque and returns it'''
        return super(Deque, self).pop()

    def pop(self):
        '''removes a value from the end of the deque and returns it'''
        return super(Deque, self).shift()

    def appendleft(self, arg):
        '''adds a value to the front of the deque'''
        super(Deque, self).push(arg)
