# -*- coding utf-8 -*-
import random


class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None):
        '''The Node initializer with a key, value, left and right child'''
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get_dot(self):
        '''
            returns the tree with root "self" as a dot graph for
            visualization
        '''
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        '''recursively prepare a dot graph entry for this node'''
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)


class BST(object):

    def __init__(self, root=None):
        '''Initialize the Tree'''
        self.size = 0
        self.depth_left = 0
        self.depth_right = 0

        self.root = root

    def insert(self, val):
        '''insert a node with with value=val'''
        # import pdb; pdb.set_trace()
        new_node = Node(value=val)
        current = self.root
        depth_right = 1
        depth_left = 1
        if self.root is None:
            self.root = new_node
        else:
            while True:
                if new_node.value > current.value:
                    depth_right += 1
                    if current.right is None:
                        current.right = new_node
                        self.depth_right = max(depth_right, self.depth_right)
                        break
                    else:
                        current = current.right
                else:
                    depth_left += 1
                    if current.left is None:
                        current.left = new_node
                        self.depth_left = max(depth_left, self.depth_left)
                        break
                    else:
                        current = current.left
        self.size += 1

    def contains(self, val):
        '''returns True if val is in the Tree'''
        current = self.root
        while True:
            if val == current.value:
                return True
            elif val > current.value:
                if current.right is None:
                    return False
                else:
                    current = current.right
            else:
                if current.left is None:
                    return False
                else:
                    current = current.left

    def depth(self):
        '''returns the total number of levels'''
        return max(self.depth_left, self.depth_right)

    def balance(self):
        '''returns the difference in size in depth of the left and right
            half of the Tree. greater depth on the left returns a positive
            value.
        '''
        return self.depth_left - self.depth_right


if __name__ == "__main__":

    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    bst.depth()

    # print(bst.root.get_dot())
