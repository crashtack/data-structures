# -*- coding utf-8 -*-
import random
from queue_ import Queue
from stack import Stack


class Node(object):
    """Implement a Node class with value, left and right."""

    def __init__(self, value=None, left=None, right=None, parent=None, _depth=1):
        """The Node initializer with a key, value, left and right child."""
        self.value = value
        self._left = left
        self._right = right
        self.parent = parent
        self._depth = _depth  # i added this during lecture

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        try:
            node.parent = self
        except AttributeError:
            pass

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        try:
            node.parent = self
        except AttributeError:
            pass

    def insert_non_balance(self, nn):   # nn =  new_node
        """Insert a node in the correct place."""
        if nn.value > self.value:
            if self.right:
                self.right.insert_non_balance(nn)
            else:
                self.right = nn
            self._depth = max(self._depth, self.right._depth + 1)

        elif nn.value < self.value:
            if self.left:
                self.left.insert_non_balance(nn)
            else:
                self.left = nn
            self._depth = max(self._depth, self.left._depth + 1)

    def insert(self, nn):   # nn =  new_node
        """Insert a node in the correct place. Rebalnce the tree"""

        if nn.value > self.value:
            if self.right:
                self.right.insert(nn)
            else:
                self.right = nn
            self._depth = max(self._depth, self.right._depth + 1)

            if self.balance() <= -2 and self.right.balance() < 0:
                self.right.pivot_left()
            if self.balance() <= -2 and self.right.balance() > 0:
                self.right.left.pivot_right()
                self.right.pivot_left()
                # self.right.pivot_rl()

        elif nn.value < self.value:
            if self.left:
                self.left.insert(nn)
            else:
                self.left = nn
            self._depth = max(self._depth, self.left._depth + 1)

            if self.balance() >= 2 and self.left.balance() > 0:
                self.left.pivot_right()
            if self.balance() >= 2 and self.left.balance() < 0:
                self.left.right.pivot_left()
                self.left.pivot_right()
                # self.left.pivot_lr()

    @property
    def depth(self):
        try:
            left_depth = self.left._depth
        except AttributeError:
            left_depth = 0
        try:
            right_depth = self.right._depth
        except AttributeError:
            right_depth = 0

        return max(left_depth, right_depth) + 1

    def balance(self):
        try:
            left_depth = self.left._depth
        except AttributeError:
            left_depth = 0
        try:
            right_depth = self.right._depth
        except AttributeError:
            right_depth = 0

        return left_depth - right_depth

    def in_order(self):
        '''recursive in order traversal'''
        if self.left:
            for item in self.left.in_order():
                yield item
        yield self.value
        if self.right:
            for item in self.right.in_order():
                yield item

    def post_order(self):
        '''recursive post order traversal'''
        if self.left:
            for item in self.left.post_order():
                yield item
        if self.right:
            for item in self.right.post_order():
                yield item
        yield self.value

    def pivot_right(self):
        """Perform a right rotation on the node."""
        pivot = self
        temp = self.parent
        sib = self._right

        if temp.parent and temp.parent < temp:
            temp.parent.right = self
        elif temp.parent:
            temp.parent.left = self
        self.parent = temp.parent
        self._right = temp
        temp.parent = self
        temp._left = sib

        if temp.right and temp.left:
            temp._depth = max(temp.right.depth, temp.left.depth) + 1
        elif temp.right:
            temp._depth = temp.right.depth + 1
        elif temp.left:
            temp._depth = temp.left.depth + 1
        else:
            temp._depth = 1

        if pivot.left:
            pivot._depth = max(pivot.right.depth, pivot.left.depth) + 1
        else:
            pivot._depth = pivot.right.depth + 1

    def pivot_left(self):
        """Perform a left rotation on the node."""
        pivot = self
        temp = self.parent
        sib = self._left

        if temp.parent and temp.parent > temp:
            temp.parent.left = self
        elif temp.parent:
            temp.parent.right = self
        self.parent = temp.parent
        self._left = temp
        temp.parent = self
        temp._right = sib

        if temp.left and temp.right:
            temp._depth = max(temp.right.depth, temp.left.depth) + 1
        elif temp.right:
            temp._depth = temp.right.depth + 1
        elif temp.left:
            temp._depth = temp.left.depth + 1
        else:
            temp._depth = 1

        if pivot.right:
            self._depth = max(self.left.depth, self.right.depth) + 1
        else:
            self._depth = self.left.depth + 1

    def pivot_rl(self):
        pivot = self
        pivot.value, pivot.left.value = pivot.left.value, pivot.value
        pivot.right = pivot.left
        pivot.left = None
        self.pivot_left()

    def pivot_lr(self):
        pivot = self
        pivot.value, pivot.right.value = pivot.right.value, pivot.value
        pivot.left = pivot.right
        pivot.right = None
        self.pivot_right()

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
            if self.root.parent:
                self.root = self.root.parent
        self.size += 1

    def insert_non_balance(self, val):
        """Insert a node with with value=val."""
        new_node = Node(value=val)
        if self.root is None:
            self.root = new_node
        else:
            perform_insert = self.root.insert_non_balance(new_node)
            if perform_insert:
                self.root = perform_insert
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
        if self.root is None:
            return 0
        else:
            return self.root.balance()

    def _traverse(self, add, remove, size):
        '''Traverse function
            takes in other functions and a start_node'''
        while size():
            x = remove()
            if x:
                add(x.left, x.right)
                yield x.value

    def breadth_first_traversal(self):
        '''perform a breadth first traversal, returns a list of
           nodes in the graph
        '''
        q = Queue()
        q.enqueue(self.root)

        def add(a, b):
            q.enqueue(a)
            q.enqueue(b)

        return self._traverse(add, q.dequeue, q.size)

    def pre_order(self):
        '''perform a breadth first traversal, returns a list of
           nodes in the graph
        '''
        s = Stack()
        s.push(self.root)

        def add(a, b):
            s.push(b)
            s.push(a)
        return self._traverse(add, s.pop, s.size)

    def in_order(self):
        '''Traverse function
            takes in other functions and a start_node'''
        if self.root:
            return self.root.in_order()
        else:
            return []

    def post_order(self):
        '''Traverse function
            takes in other functions and a start_node'''
        if self.root:
            return self.root.post_order()
        else:
            return []

    def delete(self, target):
        """a function that removes a child node"""
        # initialization
        current = self.root
        pointer = None

        # search
        while current:
            if target == current.value:
                break
            pointer = current
            if current.value < target:
                current = current.right
            else:
                current = current.left
        if current is None:
            return

        # target has 2 children
        if current.left is not None and current.right is not None:
            y = current.left
            pointer = current
            while y.right:
                pointer = y
                y = y.right
            current.value = y.value
            current = y

        # leaf and 1 child cases
        if pointer is None:  # case where there is only one node
            if current.left:
                self.root = current.left
            else:
                self.root = current.right
        if current.left:
            tmp = current.left
        else:
            tmp = current.right
        if current == pointer.right:
            pointer.right = tmp
        else:
            pointer.left = tmp


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
    # for item in worst_list:
    #     worst_case.insert(item)



    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    print(bst.root.get_dot())
