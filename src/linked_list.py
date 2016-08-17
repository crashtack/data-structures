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
        if head is not None:
            self.head = head[0]
            for i in head:
                self.push(i)
                print(u'input: {}'.format(i))
        # else:
        #     self.head = head

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
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, val):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == val:
                found = True
            else:
                current = current.get_next()
        if current is None:
            # raise ValueError("that value is not in the list")
            return None
        return current

    def remove(self, node):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_date() == node:
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
        current = self.head
        print('display current: {}'.format(current.get_data()))
        if current is None:
            return None
        else:
            fake_tuple = u'('
            while current.get_next():
                fake_tuple += u"'{}', ".format(current.get_data())
                current = current.get_next()
            fake_tuple += u"'{}'".format(current.get_data())
            fake_tuple += u')'
            print(fake_tuple)
            return fake_tuple
