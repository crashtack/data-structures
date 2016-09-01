# -*- coding utf-8 -*-
import pytest


TABLE = [
    ([(10, 'whatevs'), (5, 'WE')],
     [(5, 'WE'), (10, 'whatevs')],
     [(5, 'WE'), (7, 'test'), (10, 'whatevs')]),
    ([(6, 'whatevs'), (12, 'WE')],
     [(6, 'whatevs'), (12, 'WE')],
     [(6, 'whatevs'), (7, 'test'), (12, 'WE')]),
]

TABLE2 = [
    ([(10, 'first 10'), (5, 'first 5')],
     [(5, 'first 5'), (10, 'first 10'), (10, 'second 10')]),
    ([(6, 'first 6'), (10, 'first 10')],
     [(6, 'first 6'), (10, 'first 10'), (10, 'second 10')]),
    ([(20, 'first 20'), (10, 'first 10')],
     [(10, 'first 10'), (10, 'second 10'), (20, 'first 20')]),
    ([(1, 'first 1'), (2, 'first 2')],
     [(1, 'first 1'), (2, 'first 2'), (10, 'second 10')]),
    ([(12, 'first 12'), (20, 'first 20')],
     [(10, 'second 10'), (12, 'first 12'), (20, 'first 20')]),
]


def test_priorityq_none():
    '''Tests initialization of the priorityq class with None'''
    from priorityq import Priorityq
    pq = Priorityq()
    assert pq.priorityq is None


def test_priorityq_noniterable():
    '''Tests initialization of the priorityq class with a non-iterable'''
    from priorityq import Priorityq
    with pytest.raises(TypeError):
        pq = Priorityq(4)


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_priorityq_int(input_d, result, result2):
    '''Tests initialization of the priorityq class'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    assert pq.priorityq == result


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_insert_none(input_d, result, result2):
    '''Tests inserting none into a priority queue'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    with pytest.raises(TypeError):
        pq.insert()


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_insert(input_d, result, result2):
    '''Test the insert method'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    pq.insert((7, 'test'))
    assert pq.priorityq == result2


@pytest.mark.parametrize('input_d, result', TABLE2)
def test_insert_priority_inserts(input_d, result):
    '''Test the insert method of different priority items'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    pq.insert((10, 'second 10'))
    assert pq.priorityq == result


def test_pop_queue():
    from priorityq import Priorityq
    pq = Priorityq([(6, 'first 6'), (10, 'first 10'), (10, 'second 10')])
    pq.pop()
    assert pq.priorityq == [(10, 'first 10'), (10, 'second 10')]


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_pop_return_value(input_d, result, result2):
    '''Test that pop returns the correct value'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    assert pq.pop() == result[0]


def test_pop_none():
    from priorityq import Priorityq
    pq = Priorityq()
    with pytest.raises(IndexError):
        pq.pop()


def test_pop_no_heap():
    '''Test pop methodif the queue is empty'''
    from priorityq import Priorityq
    pq = Priorityq()
    with pytest.raises(IndexError):
        pq.pop()


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_peek(input_d, result, result2):
    '''tests the peek method'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    assert pq.peek() == result[0]

def test_peek_none():
    from priorityq import Priorityq
    pq = Priorityq()
    with pytest.raises(IndexError):
        pq.peek()










