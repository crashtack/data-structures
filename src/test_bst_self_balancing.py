# -*- coding utf-8 -*-
"""Test suite for Self Balancing Binary Search Tree."""
import pytest
from bst import BST, Node


def test_balance_node():
    this_node = Node(10)
    assert this_node.balance() == 0


def test_balance_node_lef():
    this_node = Node(10)
    this_node.left = Node(5)
    assert this_node.balance() == 1


def test_balance_node_right():
    this_node = Node(10)
    this_node.right = Node(15)
    assert this_node.balance() == -1


def test_balance_node_both():
    this_node = Node(10)
    this_node.left = Node(5)
    this_node.right = Node(15)
    assert this_node.balance() == 0


def test_balance_node_both_parent():
    this_node = Node(5)
    this_node.right = Node(7)
    this_node.right.right = Node(10)
    # import pdb; pdb.set_trace()
    this_node.right.pivot_left()
    # import pdb; pdb.set_trace()
    assert this_node.parent.parent is None


def test_left_depth():
    this_node = Node(3, _depth=4)
    this_node.left = Node(2, _depth=1)
    this_node.right = Node(5, _depth=3)
    this_node.right.left = Node(4, _depth=1)
    this_node.right.right = Node(7, _depth=7)
    this_node.right.right.right = Node(10, _depth=1)
    # import pdb; pdb.set_trace()
    assert this_node.depth == 4


def test_depth_pivot_right():
    this_node = Node(3, _depth=4)
    this_node.left = Node(2, _depth=1)
    this_node.right = Node(5, _depth=3)
    this_node.right.left = Node(4, _depth=1)
    this_node.right.right = Node(7, _depth=2)
    this_node.right.right.right = Node(10, _depth=1)
    # import pdb; pdb.set_trace()
    this_node.right.right.pivot_left()
    assert this_node.depth == 4


def test_depth_pivot_right_left():
    this_node = Node(3, _depth=4)
    this_node.left = Node(2, _depth=1)
    this_node.right = Node(5, _depth=3)
    this_node.right.left = Node(4, _depth=1)
    this_node.right.right = Node(7, _depth=2)
    this_node.right.right.right = Node(10, _depth=1)
    # import pdb; pdb.set_trace()
    this_node.right.right.pivot_left()
    assert this_node.right.depth == 3


def test_depth_pivot_right_left2():
    this_node = Node(5, _depth=3)
    this_node.right = Node(7, _depth=2)
    this_node.right.right = Node(9, _depth=1)
    this_node.right.pivot_left()
    assert this_node.parent.depth == 2


def test_right_rotation():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(3)
    bst.insert_non_balance(1)
    bst.root.left.pivot_right()
    assert bst.root.left is None


def test_right_rotation2():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(3)
    bst.insert_non_balance(1)
    bst.root.left.pivot_right()
    assert bst.root.parent.value == 3


def test_right_rotation3():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(3)
    bst.insert_non_balance(1)
    bst.root.left.pivot_right()
    assert bst.root.parent.left.value == 1


def test_left_rotation():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(7)
    bst.insert_non_balance(10)
    bst.root.right.pivot_left()
    assert bst.root.left is None


def test_left_rotation2():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(7)
    bst.insert_non_balance(10)
    bst.root.right.pivot_left()
    assert bst.root.parent.value is 7


def test_left_rotation3():
    bst = BST()
    bst.insert_non_balance(5)
    bst.insert_non_balance(7)
    bst.insert_non_balance(10)
    bst.root.right.pivot_left()
    assert bst.root.parent.right.value is 10


def test_pivot_left_root_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    # bst.root.right.pivot_left()
    assert bst.root.value is 7


def test_pivot_left_left_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    # bst.root.right.pivot_left()
    assert bst.root.left.value is 5


def test_pivot_left_right_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    # bst.root.right.pivot_left()
    assert bst.root.right.value is 10


def test_pivot_left_depth():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    # bst.root.right.pivot_left()
    assert bst.depth() == 2


def test_pivot_left_balance():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    assert bst.balance() == 0


def test_pivot_left_balance():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    assert bst.root.parent is None


def test_pivot_right_root_value():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    assert bst.root.value is 3


def test_pivot_right_left_value():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    assert bst.root.left.value is 2


def test_pivot_right_right_value():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    assert bst.root.right.value is 5


def test_pivot_right_depth():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    assert bst.depth() == 2


def test_pivot_right_balance():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    assert bst.balance() == 0


def test_pivot_rl_root_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    assert bst.root.value is 6


def test_pivot_rl_left_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    assert bst.root.left.value is 5


def test_pivot_rl_right_value():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    assert bst.root.right.value is 7


def test_pivot_rl_depth():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    assert bst.depth() == 2


def test_pivot_rl_balance():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    assert bst.balance() == 0


def test_pivot_lr_root_value():
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.value is 3


def test_pivot_lr_left_value():
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.left.value is 2


def test_pivot_lr_right_value():
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.right.value is 5


def test_pivot_lr_right_value():
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.parent is None


# def test_pivot_lr_depth():
#     bst = BST()
#     bst.insert(5)
#     bst.insert(7)
#     bst.insert(6)
#     assert bst.depth() == 2
#
#
# def test_pivot_lr_balance():
#     bst = BST()
#     bst.insert(5)
#     bst.insert(7)
#     bst.insert(6)
#     assert bst.balance() == 0
#
#
# def test_pivot_lr_root_no_parent():
#     bst = BST()
#     bst.insert(5)
#     bst.insert(7)
#     bst.insert(6)
#     assert bst.root.parent is None
