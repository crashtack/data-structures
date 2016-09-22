# -*- coding utf-8 -*-
import pytest

def test_include():
    """test to see if insert can be included"""
    from insert import insert


def test_return_list():
    """Test to see if a list is returned from the insert function."""
    from insert import insert
    my_list = insert([])
    assert type(my_list) is list

def test_sort_one_item():
    """Test if one item is inputted if that same list is recieved back."""
    from insert import insert
    my_list = insert([5])
    assert my_list == [5]

def test_insert_non_list():
    """Test if an error is raised if not passed in a list."""
    from insert import insert
    with pytest.raises(TypeError):
        insert('a')

def test_sort_two_items():
    """Test to see if inputed a string of two items that the list is sorted."""
    from insert import insert
    my_list = [1, 2]
    assert insert(my_list) == sorted(my_list)

def test_sort_two_items_reverse():
    """Test to see if inputed a string of two items that the list is sorted."""
    from insert import insert
    my_list = [2, 1]
    assert insert(my_list) == sorted(my_list)


def test_sort_multi_items_reverse():
    """Test to see if inputed a string of two items that the list is sorted."""
    from insert import insert
    my_list = [5, 2, 3, 7]
    assert insert(my_list) == sorted(my_list)


