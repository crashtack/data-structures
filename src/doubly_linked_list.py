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
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre_node = new_node
            new_node.next_node = self.head
            new_node.pre_node = None
            self.head = new_node

    def append(self, val):
        ''' append a node onto the tail of the list '''
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.pre_node = self.tail
            new_node.next_node = None
            self.tail = new_node

    def pop(self):
        """pops a node of the head of the list"""
        try:
            returned_value = self.head.data
        except AttributeError:
            raise IndexError('can not pop from empty list')
        self.head = self.head.next_node
        try:
            self.head.pre_node = None
        except AttributeError:
            pass
        return returned_value

    def shift(self):
        """removes a node of the tail of the list"""
        try:
            returned_value = self.tail.data
        except AttributeError:
            raise IndexError('can not remove from empty list')
        self.tail = self.tail.pre_node
        try:
            self.tail.next_node = None
        except AttributeError:
            pass
        return returned_value

    def remove(self, val):
        """removes the passed value if it is pressent in the list"""
        # import pdb; pdb.set_trace()
        current_node = self.head
        previous = None
        found = False
        try:
            while current_node.data is not val:
                # this if looks for the correct node
                current_node = current_node.next_node

                if current_node.pre_node is not None:
                    current_node = current_node.next_node
                    current_node = current_node.pre_node
                    return current_node.data
                else:
                    self.head = current_node.next_node
                    current_node = None
                if current_node is None:
                    raise ValueError("that value is not in the list")


        # current_node = current_node.next_node
        #
        #
        #     previous = current
        #             current = current.next_node
        # if current is None:
        #     raise ValueError("that value is not in the list")
        # if previous is None:
        #     # This is where the actual removing happens
        #     if pre_node == None:
        #         self.head = current.next_node
        #     elif next_node == None:
        #         self.tail.data = tail.pre_node
        #         self.tail.next_node = None
        # else:
        #     previous.next_node = (current.next_node)
