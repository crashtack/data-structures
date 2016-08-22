# -*- coding utf-8 -*-
import pytest


def test_none():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    print('head: {}'.format(dll.head))
    assert (dll.head is None) and (dll.tail is None)


def test_push():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    print('dll.head.data: {}'.format(dll.head.data))
    assert dll.head.data == 'bob'


def test_push_somethingallreadythere():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.push('dog')
    print('head: {}'.format(dll.head))
    assert dll.head.data == 'dog'


def test_append():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append('bob')
    assert dll.tail.data == 'bob'


def test_append_somethingallreadythere():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append('bob')
    dll.append('dog')
    assert dll.tail.data == 'dog'


def test_pop_empty():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.pop()


def test_pop():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    assert dll.pop() == 'bob'


def test_pop_2():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.push('fred')
    assert dll.pop() == 'fred'


def test_pop_3():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.push('fred')
    dll.pop()
    assert dll.head.data == 'bob'


def test_shift_empty():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.shift()


def test_shift():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    assert dll.shift() == 'bob'


def test_shift_2():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.push('fred')
    assert dll.shift() == 'bob'


def test_shift_3():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.push('fred')
    dll.shift()
    assert dll.tail.data == 'fred'


def test_remove_no_list():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.remove('bob')


def test_remove_1_removed():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    dll.remove('bob')
    assert dll.head is None


def test_remove_1_not_found():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('bob')
    with pytest.raises(ValueError):
        dll.remove('fred')


def test_remove_multi_removed_head():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['zeek', 'bob', 'james', 'sam'])
    dll.remove('sam')
    assert dll.search('sam') is None


def test_remove_multi_removed_tail():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['zeek', 'bob', 'james', 'sam'])
    dll.remove('zeek')
    assert dll.search('zeek') is None


def test_remove_multi_removed_mid():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['seek', 'bob', 'james', 'sam'])
    dll.remove('bob')
    assert dll.search('bob') is None


def test_remove_multi_not_found():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['seek', 'bob', 'james', 'sam'])
    with pytest.raises(ValueError):
        dll.remove('fred')


def test_search_found():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['seek', 'bob', 'james', 'sam'])
    assert dll.search('bob').data == 'bob'


def test_search_not_found():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList(['seek', 'bob', 'james', 'sam'])
    assert dll.search('nick') is None


def test_search_empty():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    assert dll.search('nick') is None
