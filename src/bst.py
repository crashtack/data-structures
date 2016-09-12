# -*- coding utf-8 -*-


class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None):
        '''The Node initializer with a key, value, left and right child'''
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST(object):

    def __init__(self, root=None):
        '''Initialize the Tree'''
        self.size = 0
        self.root = root

    def insert(self, val):
        '''insert a node with with value=val'''
        new_node = Node(value=val)
        current = self.root
        if self.root is None:
            self.root = new_node
        else:
            while True:
                if new_node.value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left






        self.size += 1

    def contains(self, val):
        '''returns True if val is in the Tree'''
        pass

    def depth(self):
        '''returns the total number of levels'''
        pass

    def balance(self):
        '''returns the difference in size in depth of the left and right
            half of the Tree. greater depth on the left returns a positive
            value.
        '''
        pass
