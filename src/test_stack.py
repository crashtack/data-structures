# -*- coding utf-8 -*-
import pytest


# This test push and pop
def test_push_pop():
    from stack import Stack
    test_stack = Stack()
    test_stack.push('bob')
    assert test_stack.pop() == 'bob'

def test_push():
    from stack import Stack
    test_stack = Stack()
    test_stack.push('bob')
    test_stack.push('james')

    assert test_stack._linked_list.size() == 2


def test_init_list():
    from stack import Stack
    test_stack = Stack(['bob', 'zeek'])
    assert test_stack.pop() == 'zeek'
    assert test_stack.pop() == 'bob'

def test_push_pop():
    from stack import Stack
    test_stack = Stack()
    with pytest.raises(IndexError):
        test_stack.pop()
