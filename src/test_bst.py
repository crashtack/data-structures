# -*- coding utf-8 -*-
"""Test suite for Binary Search Tree."""
import pytest
import random
from bst import BST, Node


@pytest.fixture
def known_bst():
    """Test fixture for a binary search tree."""
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    return bst, 3, 0

@pytest.fixture
def straight_bst():
    """Test fixture for a binary search tree."""
    bst = BST()
    for i in range(1, 10):
        bst.insert(i)
    return bst, 10, -9

FDSA = [
    ([5, 4, 2, 8, 7, 9], 3, 0, [5, 4, 8, 2, 7, 9], [5, 4, 2, 8, 7, 9], [2, 4, 7, 9, 8, 5]),
    ([4, 9, 3, 5, 5, 8, 6, 2, 4], 5, -2, [4, 3, 9, 2, 5, 8, 6], [4, 3, 2, 9, 5, 8, 6], [2, 3, 6, 8, 5, 9, 4]),
    ([5, 5, 6, 9, 8, 2, 8, 2, 8], 4, -2, [5, 2, 6, 9, 8], [5, 2, 6, 9, 8], [2, 8, 9, 6, 5]),
    ([7, 6, 2, 2, 2, 9, 9, 5, 9], 4, 2, [7, 6, 9, 2, 5], [7, 6, 2, 5, 9], [5, 2, 6, 9, 7]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 4, -2, [3, 1, 8, 5, 9, 6], [3, 1, 8, 5, 6, 9], [1, 6, 5, 9, 8, 3]),
    ([-14, -43, 48, -10, -98, 94, -71, 35, 75, 73, -64, -35, -14, -87,
        -81, 90, -41, -68, -28], 6, 1, [-14, -43, 48, -98, -35, -10, 94, -71, -41, -28, 35, 75, -87, -64, 73, 90, -81, -68], [-14, -43, -98, -71, -87, -81, -64, -68, -35, -41, -28, 48, -10, 35, 94, 75, 73, 90], [-81, -87, -68, -64, -71, -98, -41, -28, -35, -43, 35, -10, 73, 90, 75, 94, 48, -14]),
    (['w', 'p', 'R', 'N', 'U', 's', 'q', 'w', 'y', 'i', 'l', 'k', 'N',
        'O', 'k', 'd', 'v', 'c', 'u'], 7, 6, list('wpyRsNUqvOiudlck'), list('wpRNOUidclksqvuy'), list('ONcdkliURquvspyw')),
    ([], 0, 0, [], [], [])
]


DELET = [
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 14, [3, 1, 8, 5, 9, 6]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 1, [3, 8, 5, 9, 6]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 6, [3, 1, 8, 5, 9]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 5, [3, 1, 8, 6, 9]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 9, [3, 1, 8, 5, 6]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 8, [3, 1, 6, 5, 9]),
    ([3, 1, 8, 5, 1, 6, 3, 9, 3], 3, [1, 8, 5, 9, 6]),
]


@pytest.fixture(params=FDSA)
def our_bsts(request):
    from bst import BST
    bst = BST()
    for item in request.param[0]:
        bst.insert(item)
    return bst, request.param[1], request.param[2], request.param[3], request.param[4], request.param[0], request.param[5]


@pytest.fixture(params=DELET)
def delete_bst(request):
    from bst import BST
    bst = BST()
    for item in request.param[0]:
        bst.insert(item)
    return bst, request.param[1], request.param[2]


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


def test_coontains(known_bst):
    """Check to see if 7 is in the test bst."""
    assert known_bst[0].contains(7) is True


def test_coontains_false(known_bst):
    """Check to see if 6 is not in the test bst."""
    assert known_bst[0].contains(6) is False


def test_coontains_false_2(known_bst):
    """Check to see if 6 is not in the test bst."""
    assert known_bst[0].contains(15) is False


def test_depth(known_bst):
    """check the depth of the left branch"""
    assert known_bst[0].depth() == 3


def test_depth_empty():
    """check the depth of an empty graph"""
    bst = BST()
    assert bst.depth() == 0


def test_balance_known_tree(known_bst):
    """check the depth of the left branch"""
    assert known_bst[0].balance() == 0


def test_balance_known_tree_2(known_bst):
    """check the depth of the left branch"""
    known_bst[0].insert(12)
    assert known_bst[0].balance() == known_bst[2] - 1


def test_balance_right2(our_bsts):
    """test the balance method"""
    assert our_bsts[0].depth() == our_bsts[1]


def test_depth_known(our_bsts):
    """test the depth method"""
    assert our_bsts[0].depth() == our_bsts[1]


def test_balance_empty():
    """test a balance of a empty tree."""
    bst = BST()
    assert bst.balance() == 0


def test_breath_first_traversal(our_bsts):
    """test that breadtch first traversal work"""
    bft = []
    for i in our_bsts[0].breadth_first_traversal():
        bft.append(i)
    assert bft == our_bsts[3]


def test_pre_order_traversal(our_bsts):
    """test that breadtch first traversal work"""
    bpo = []
    for i in our_bsts[0].pre_order():
        bpo.append(i)
    assert bpo == our_bsts[4]


def test_in_order_traversal(our_bsts):
    """test that breadtch first traversal work"""
    bio = []
    for i in our_bsts[0].in_order():
        bio.append(i)
    assert bio == sorted(list(set(our_bsts[5])))


def test_post_order_traversal(our_bsts):
    """test that breadtch first traversal work"""
    bpost = []
    for i in our_bsts[0].post_order():
        bpost.append(i)
    assert bpost == our_bsts[6]


def test_delete_node(delete_bst):
    bst = []
    delete_bst[0].delete(delete_bst[1])
    for i in delete_bst[0].breadth_first_traversal():
        bst.append(i)
    assert bst == delete_bst[2]


def test_right_rotation():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.root.left.pivot_right()
    assert bst.root.left is None


def test_right_rotation2():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.root.left.pivot_right()
    assert bst.root.parent.value == 3


def test_right_rotation3():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.root.left.pivot_right()
    assert bst.root.parent.left.value == 1


def test_left_rotation():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    bst.root.right.pivot_left()
    assert bst.root.left is None


def test_left_rotation2():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    bst.root.right.pivot_left()
    assert bst.root.parent.value is 7


def test_left_rotation3():
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    bst.root.right.pivot_left()
    assert bst.root.parent.right.value is 10


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


