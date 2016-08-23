# -*- coding utf-8 -*-
import pytest

ITERABLE_TABLE = [
    (None, None, [9]),
    ([1], [1], [1, 9]),
    ([4, 6, 5, 3], [3, 4, 5, 6], [3, 4, 5, 6, 9]),
    ([15, 11, 12, 10], [10, 11, 12, 15], [9, 10, 11, 12, 15]),
    ([15, 11, 5, 10], [5, 10, 11, 15], [5, 9, 10, 11, 15]),
]

POP_TABLE = [
    ([1], 1, []),
    ([4, 6, 5, 3], 3, [4, 5, 6]),
    ([15, 11, 12, 10], 10, [11, 12, 15]),
    ([15, 11, 5, 10], 5, [10, 11, 15]),
]


@pytest.mark.parametrize('init_list, result, result2', ITERABLE_TABLE)
def test_binheap_int(init_list, result, result2):
    '''Tests initialization of the heap class'''
    from binheap import Binheap
    bh = Binheap(init_list)
    # print(bh.heap)
    assert bh.heap == result


@pytest.mark.parametrize('init_list, result, result2', ITERABLE_TABLE)
def test_push(init_list, result, result2):
    '''Test the push function'''
    from binheap import Binheap
    bh = Binheap(init_list)
    bh.push(9)
    assert bh.heap == result2


@pytest.mark.parametrize('init_list, pop_return, heap', POP_TABLE)
def test_pop_return_value(init_list, pop_return, heap):
    '''Test that pop returns the correct value'''
    from binheap import Binheap
    bh = Binheap(init_list)
    assert bh.pop() == pop_return


@pytest.mark.parametrize('init_list, pop_return, heap', POP_TABLE)
def test_pop_heap(init_list, pop_return, heap):
    '''Test that pop mutates the heap'''
    from binheap import Binheap
    bh = Binheap(init_list)
    bh.pop()
    assert bh.heap == heap
