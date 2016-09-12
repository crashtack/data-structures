# -*- coding utf-8 -*-


def test_include():
    '''test that BST can be included'''
    from bst import BST


def test_init_size():
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.size == 0


def test_init_root():
    from bst import BST
    bst = BST()
    # import pdb; pdb.set_trace()
    assert bst.root is None


def test_insert():
    from bst import BST
    bst = BST()
    bst.insert(1)
    assert bst.size == 1


def test_insert2():
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.left.value == 2


def test_insert3():
    from bst import BST
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    assert bst.root.right is None


def test_insert4():
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
