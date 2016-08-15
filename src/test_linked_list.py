# -*- coding utf-8 -*-
import pytest


def test_push():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    assert ll.head.get_data() == 'bob'


def test_pop():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    assert ll.pop() == 'bob'


def test_pop_empty():
    from linked_list import LinkedList
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop()



# def test_pop1():
#     from linked_list import LinkedList
#     ll = LinkedList()
#     ll.push('fred')
#     ll.pop()
#     assert ll.lst == ['bob']
#
#
# def test_size():
#     from linked_list import LinkedList
#     print(ll)

# def test_search():
#     from linked_list import search
#
#
# def test_remove():
#     from linked_list import remove
#
#
# def test_display():
#     from linked_list import display
