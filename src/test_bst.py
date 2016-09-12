# -*- coding utf-8 -*-
"""Test suite for Binary Search Tree."""
import pytest
from bst import BST


@pytest.fixture
def test_bst():
    """Test fixture for a binary search tree."""
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    return bst


def test_include():
    """Test that BST can be included."""
    from bst import BST


def test_init_size():
    """Test initial size."""
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.size == 0


def test_init_root():
    """Test BST initialize root as None."""
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.root is None


def test_insert_size():
    """Test size increments on insert."""
    from bst import BST
    bst = BST()
    bst.insert(1)
    assert bst.size == 1


def test_insert_value():
    """Test that an inserted node has correct value."""
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.left.value == 2


def test_insert_right_node_None():
    """Test to see if inserted node does not change other node."""
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.right is None


def test_insert_second_depth_level():
    """Test to see if inserted node goes to the correct place."""
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    assert bst.root.left.right.value == 3


def test_insert_check_size():
    """Check to see if size is correct after several inserts."""
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    assert bst.size == 3


def test_coontains(test_bst):
    """Check to see if 7 is in the test bst."""
    assert test_bst.contains(7) is True


def test_coontains_false(test_bst):
    """Check to see if 6 is not in the test bst."""
    assert test_bst.contains(6) is False
