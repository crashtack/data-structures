# -*- coding utf-8 -*-
import pytest

ITERABLE_TABLE = [
    None,
    ['string'],
    'strings are itearble',
    (4, 45, 6, 7),
    [4, 5, 6, 4, 3, 5],
]
#
# @pytest.fixture
# def deque_with_vals():
#     from queue_ import Queue
#     q_with_vals = Queue(['sam', 'tim', 'tom'])
#     return q_with_vals


def test_deque():
    from deque import Deque
    assert 0 == 0


def test_deque_empty():
    from deque import Deque
    d = Deque()
    assert d.size() == 0


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_initialize(iterable):
    from deque import Deque
    d = Deque(iterable)
    try:
        assert d.size() == len(iterable)
    except TypeError:
        assert d.size() == 0


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_append(iterable):
    from deque import Deque
    d = Deque(iterable)
    d.append('something')
    assert d.tail.data == 'something'


def test_deque_size():
    from deque import Deque
    d = Deque()
    assert d.size() == 0


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_appendleft(iterable):
    from deque import Deque
    d = Deque(iterable)
    d.appendleft('something')
    assert d.head.data == 'something'


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_appendleft_twice(iterable):
    from deque import Deque
    d = Deque(iterable)
    d.appendleft('something')
    d.appendleft(43)
    assert d.head.data == 43


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_pop(iterable):
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        assert d.pop() == iterable[0]
    else:
        with pytest.raises(IndexError):
            d.pop()


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_popleft(iterable):
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        assert d.popleft() == iterable[-1]
    else:
        with pytest.raises(IndexError):
            d.popleft()
