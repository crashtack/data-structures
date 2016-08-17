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
        self.head = None
        if head is not None:
            for i in head:
                self.push(i)

    def push(self, val):
        """Push a node onto the head of the list"""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        """pops a node of the head of the list"""
        try:
            returned_value = self.head.get_data()
        except AttributeError:
            raise IndexError('can not pop from empty LinkedList')
        self.head = self.head.get_next()
        return returned_value

    def size(self):
        """Returns the number of items in the list"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, val):
        """searches the list for the value that is passed"""
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == val:
                found = True
            else:
                current = current.get_next()
        return current

    def remove(self, node):
        """removes the passed value if it is pressent in the list"""
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == node:
                found = True
            else:
                previous = current
                current = current.get_next
        if current is None:
            raise ValueError("that value is not in the list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def display(self):
        """displays the list as if it were a tuple"""
        current = self.head
        if current is None:
            return None
        else:
            fake_tuple = u'('
            while current.get_next():
                fake_tuple += u"'{}', ".format(current.get_data())
                current = current.get_next()
            fake_tuple += u"'{}')".format(current.get_data())
            print(fake_tuple)
            return fake_tuple
