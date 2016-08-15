# -*- coding utf-8 -*-


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        try:
            returned_value = self.head.get_data()
        except AttributeError:
            raise IndexError('can not pop from empty LinkedList')
        self.head = self.head.get_next()
        return returned_value

    def size(self):
        return len(self.lst)

    def search(val):
        pass

    def remove(node):
        pass

    def display():
        pass
