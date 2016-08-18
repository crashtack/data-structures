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


def test_remove_1():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('zeek')
    dll.push('fred')
    dll.remove('zeek')
    assert dll.shift() != 'fred'
