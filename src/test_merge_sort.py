# -*- coding utf-8 -*-
import pytest
import random

def test_include():
    """test to see if merge_sort can be included"""
    from merge_sort import merge_sort


def test_return_list():
    """Test to see if a list is returned from the merge_sort function."""
    from merge_sort import merge_sort
    my_list = merge_sort([])
    assert type(my_list) is list

# def test_sort_one_item():
#     """Test if one item is inputted if that same list is recieved back."""
#     from merge_sort import merge_sort
#     my_list = merge_sort([5])
#     assert my_list == [5]

# def test_merge_sort_non_list():
#     """Test if an error is raised if not passed in a list."""
#     from merge_sort import merge_sort
#     with pytest.raises(TypeError):
#         merge_sort('a')

# def test_sort_two_items():
#     """Test to see if inputed a string of two items that the list is sorted."""
#     from merge_sort import merge_sort
#     my_list = [1, 2]
#     assert merge_sort(my_list) == sorted(my_list)

# def test_sort_two_items_reverse():
#     """Test to see if inputed a string of two items that the list is sorted."""
#     from merge_sort import merge_sort
#     my_list = [2, 1]
#     assert merge_sort(my_list) == sorted(my_list)


# def test_sort_multi_items():
#     """Test to see if inputed a string of a few items that the list is sorted."""
#     from merge_sort import merge_sort
#     my_list = [5, 2, 3, 7]
#     assert merge_sort(my_list) == sorted(my_list)


# def test_sort_multi_items_2():
#     """Test to see if inputed a string of a few items that the list is sorted."""
#     from merge_sort import merge_sort
#     my_list = [random.randint(0, 100) for i in range(100)]
#     assert merge_sort(my_list) == sorted(my_list)



