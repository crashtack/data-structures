# -*- coding utf-8 -*-
import random


class Node(object):
    """Implement a Node class with value, left and right."""

    def __init__(self, key=None, value=None, left=None, right=None):
        """The Node initializer with a key, value, left and right child."""
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.depth = 1  # i added this during lecture

    def insert(self, nn):   # nn =  new_node
        """Insert a node in the correct place."""
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

    def get_dot(self):          # pragma: no cover
        """
            Return the tree with root "self" as a dot graph for
            visualization.
        """
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):         # pragma: no cover
        """Recursively prepare a dot graph entry for this node."""
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
    """Binary Search Tree class."""

    def __init__(self, root=None):
        """Initialize the Tree."""
        # TODO: what happens when bst = BST(7) is called
        # self.root = Node(value=root)
        self.size = 0
        self.root = root

    def insert(self, val):
        """Insert a node with with value=val."""
        new_node = Node(value=val)

        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

        self.size += 1

    def contains(self, val):
        """Return True if val is in the Tree."""
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
        """Return the total number of levels."""
        if self.root:
            return self.root.depth
        else:
            return 0

    def balance(self):
        """
            Return the difference in size in depth of the left and right
            half of the Tree. greater depth on the left returns a positive
            value.
        """
        try:
            depth_left = self.root.left.depth
        except AttributeError:
            depth_left = 0

        try:
            depth_right = self.root.right.depth
        except AttributeError:
            depth_right = 0

        return depth_left - depth_right


if __name__ == "__main__":          # pragma: no cover
    # Best Case Senario
    # Binary Tree built in a way that every node is balanced.
    # With this tree every iteration you can eliminate half of the
    # reamianing possiblities, until you find the value.  In the below example
    # the most values you would have to check would be 4. If you had 65,535
    # values the most you would have to check would be 16 until you found
    # the correct value. The time complexity for this senario is O(log(n))

    best_case = BST()
    best_list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for item in best_list:
        best_case.insert(item)

    # Worst Case Senario
    # Binary Tree built in a way that only has one branch. Each node has
    # only a single left or right child. In this senario you could have to
    # traverse through the whole tree to see if your value is there or not.
    # In the tree below one woulf have to check 7 nodes before finding the
    # value 11.  The time complexity for this senario is O(n)

    worst_case = BST()
    worst_list = [2, 5, 8, 14, 12, 10, 11]
    for item in worst_list:
        worst_case.insert(item)




    # print(bst.root.get_dot())
