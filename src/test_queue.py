# -*- coding utf-8 -*-
import pytest


@pytest.fixture
def empty_queue():
    from queue_ import Queue
    empty_queue = Queue()
    return empty_queue


@pytest.fixture
def q_with_vals():
    from queue_ import Queue
    q_with_vals = Queue(['sam', 'tim', 'tom'])
    return q_with_vals


def test_enqueue_empty(empty_queue):
    '''Test enquing if queue is emplty'''
    empty_queue.enqueue('bob')
    assert empty_queue.back.data == 'bob'


def test_enqueue(q_with_vals):
    '''Test enquing if there is already a queue'''
    q_with_vals.enqueue('bob')
    assert q_with_vals.back.data == 'bob'


def test_dequeue_empty(empty_queue):
    '''test deque if que is emplty'''
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_dequeue(q_with_vals):
    '''test deque if que has values'''
    assert q_with_vals.dequeue() == 'sam'


def test_peek(q_with_vals):
    '''test deque if que has values'''
    assert q_with_vals.peek() == 'sam'
