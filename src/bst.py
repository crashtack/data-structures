# -*- coding utf-8 -*-
import random


class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None):
        '''The Node initializer with a key, value, left and right child'''
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.depth = 1  # i added this during lecture

    def insert(self, nn):   # nn =  new_node
        if nn.value > self.value:
            if self.right:
                self.right.insert(nn)
            else:
                self.right = nn
            self.depth = max(self.depth, self.right.depth + 1)
        elif nn.value < self.value:
            if self.left:
                self.left.insert(nn)
            else:
                self.left = nn
            self.depth = max(self.depth, self.left.depth + 1)

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
        # TODO: what happens when bst = BST(7) is called
        # self.root = Node(value=root)
        self.size = 0
        self.root = root

    def insert(self, val):
        '''insert a node with with value=val'''
        new_node = Node(value=val)

        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

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
        if self.root:
            return self.root.depth
        else:
            return 0

    def balance(self):
        '''returns the difference in size in depth of the left and right
            half of the Tree. greater depth on the left returns a positive
            value.
        '''
        if self.root.left.depth is None:
            depth_left = 0
        else:
            depth_left = self.root.left.depth

        if self.root.right.depth is None:
            depth_right = 0
        else:
            depth_right = self.root.right.depth
        return depth_left - depth_right


if __name__ == "__main__":

    bst = BST()
    my_list = [3, 1, 8, 5, 1, 6, 3, 9, 3]
    for item in my_list:
        bst.insert(item)

    print(bst.root.get_dot())




    # print(bst.root.get_dot())
