# -*- coding utf-8 -*-
import pytest

ITERABLE_TABLE = [
    (None, None, [9]),
    ([1], [1], [1, 9]),
    ([4, 6, 5, 3], [3, 4, 5, 6], [3, 4, 5, 6, 9]),
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


# def test_push():
#     from binheap import Binheap
#     bh = Binheap([1])
#     bh.push(9)
#     assert bh.heap == [1, 9]
