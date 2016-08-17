# -*- coding utf-8 -*-


def test_push_none():
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    print('head: {}'.format(dll.head))
    assert dll.head is None


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
