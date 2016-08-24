# -*- coding utf-8 -*-
import pytest


TABLE = [
    (None, None, [(7, 'test')]),
    ([(10, 'whatevs'), (5, 'WE')], [(5, 'WE'), (10, 'whatevs')], [(5, 'WE'), (7, 'test'), (10, 'whatevs')]),
    ([(6, 'whatevs'), (12, 'WE')], [(6, 'whatevs'), (12, 'WE')], [(6, 'whatevs'), (7, 'test'), (12, 'WE')]),
]


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_priorityq_int(input_d, result, result2):
    '''Tests initialization of the priorityq class'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    assert pq.priorityq == result


@pytest.mark.parametrize('input_d, result, result2', TABLE)
def test_insert(input_d, result, result2):
    '''Test the insert method'''
    from priorityq import Priorityq
    pq = Priorityq(input_d)
    pq.insert((7, 'test'))
    assert pq.priorityq == result2
