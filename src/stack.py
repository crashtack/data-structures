# -*- coding utf-8 -*-
from linked_list import LinkedList


class Stack(object):

    def __init__(self, input=None):
        self._linked_list = LinkedList(input)

    def pop(self):
        """pops the vlaue of the top of the stack"""
        return self._linked_list.pop()

    def push(self, val):
        """pushes a value onto the top of the stack"""
        return self._linked_list.push(val)
