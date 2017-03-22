# -*- coding utf-8 -*-
import pytest
import random

def test_include():
    """test to see if insert can be included"""
    from quick import quick


def test_return_list():
    """Test to see if a list is returned from the insert function."""
    from quick import quick
    my_list = quick([])
    assert type(my_list) is list

def test_sort_one_item():
    """Test if one item is inputted if that same list is recieved back."""
    from quick import quick
    my_list = quick([5])
    assert my_list == [5]

def test_sort_non_list():
    """Test if an error is raised if not passed in a list."""
    from quick import quick
    with pytest.raises(TypeError):
        quick('a')

def test_sort_two_items():
    """Test to see if inputed a string of two items that the list is sorted."""
    from quick import quick
    my_list = [1, 2]
    assert quick(my_list) == sorted(my_list)

def test_sort_two_items_reverse():
    """Test to see if inputed a string of two items that the list is sorted."""
    from quick import quick
    my_list = [2, 1]
    assert quick(my_list) == sorted(my_list)

def test_sort_three_items_reverse():
    """Test to see if inputed a string of three items that the list is sorted."""
    from quick import quick
    my_list = [2, 1, 3]
    assert quick(my_list) == sorted(my_list)


def test_sort_multi_items():
    """Test to see if inputed a string of a few items that the list is sorted."""
    from quick import quick
    my_list = [5, 2, 3, 7, 5]
    assert quick(my_list) == sorted(my_list)


def test_sort_multi_items_2():
    """Test to see if inputed a string of a few items that the list is sorted."""
    from quick import quick
    my_list = [random.randint(0, 100) for i in range(100)]
    assert quick(my_list) == sorted(my_list)

