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
        '''Push a node onto the head of the list'''
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def append(self, val):
        '''Append a node onto the tail of the list'''
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.pre_node = self.tail
            self.tail = new_node

    def pop(self):
        '''Pops a node off the head of the list'''
        try:
            returned_value = self.head.data
        except AttributeError:
            raise IndexError('Can not pop from empty list.')
        self.head = self.head.next_node
        try:
            self.head.pre_node = None
        except AttributeError:
            pass
        return returned_value

    def shift(self):
        '''Removes a node off the tail of the list'''
        try:
            returned_value = self.tail.data
        except AttributeError:
            raise IndexError('Can not remove from empty list.')
        self.tail = self.tail.pre_node
        try:
            self.tail.next_node = None
        except AttributeError:
            pass
        return returned_value

    def search(self, val):
        '''Searches the list for the value that is passed'''
        current = self.head
        while current:
            if current.data == val:
                return current
            else:
                current = current.next_node
        return current

    def remove(self, val):
        '''Removes the passed value if it is pressent in the list'''
        if not self.head:
            raise ValueError('No list')
        found_node = self.search(val)
        if found_node:
            if found_node.pre_node:
                found_node.pre_node.next_node = found_node.next_node
            else:
                self.head = self.head.next_node
            if found_node.next_node:
                found_node.next_node.pre_node = found_node.pre_node
            else:
                self.tail = self.tail.pre_node
        else:
            raise ValueError('Value not found')
