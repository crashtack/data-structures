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
    print("search fred: {}".format(ll.search('fred')))
    assert ll.search('fred').data == 'fred'


def test_search_none():
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.search('fred') is None


def test_display():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('bob')
    ll.push('fred')
    assert ll.display() == "('fred', 'bob')"


def test_display_one_node():
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('fred')
    assert ll.display() == "('fred')"


def test_display_no_nodes():
    from linked_list import LinkedList
    ll = LinkedList()
    # ll.push('fred')
    assert ll.display() is None


def test_init_list():
    from linked_list import LinkedList
    ll = LinkedList(['bob', 'zeek'])
    # ll.push('fred')
    print(u'll: {}'.format(ll.display()))
    # assert ll.size() == 3
    assert ll.display() == "('zeek', 'bob')"
