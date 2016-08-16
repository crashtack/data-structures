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


def test_size():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    ll.push('fred')
    assert ll.size() == 2


def test_search():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    ll.push('fred')
    assert ll.search('fred') == 'fred'


def test_search_none():
    from linked_list import LinkedList
    ll = LinkedList()
    # assert ll.search('fred') == 'ValueError: that value is not in the list'
    assert ll.search('fred') == ValueError


def test_display():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    ll.push('fred')
    assert ll.display() == "('bob', 'fred')"


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
