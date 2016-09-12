# -*- coding utf-8 -*-
import pytest
from bst import BST

@pytest.fixture
def init_BST():
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    return bst


def test_include():
    '''test that BST can be included'''
    from bst import BST


def test_init_size():
    '''test initial size'''
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.size == 0


def test_init_root():
    '''test BST initialize root as None'''
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.root is None


def test_insert_size():
    '''test size increments on insert.'''
    from bst import BST
    bst = BST()
    bst.insert(1)
    assert bst.size == 1


def test_insert_value():
    '''test that an inserted node has correct value.'''
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.left.value == 2


def test_insert_right_node_None():
    '''test to see if inserted node does not change other node.'''
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.right is None


def test_insert_depth():
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.left.right.value == 3


def test_insert5():
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    assert bst.size == 3


def test_coontains(init_BST):
    assert init_BST.contains(7) is True


def test_coontains_false(init_BST):
    assert init_BST.contains(6) is False
