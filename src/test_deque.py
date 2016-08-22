# -*- coding utf-8 -*-
import pytest

ITERABLE_TABLE = [
    None,
    ['string'],
    'strings are itearble',
    (4, 45, 6, 7),
    [4, 5, 6, 4, 3, 5],
]


def test_deque_empty():
    '''Test size methood on an empty deque'''
    from deque import Deque
    d = Deque()
    assert d.size() == 0


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_initialize(iterable):
    '''test the initialize methood with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    try:
        assert d.size() == len(iterable)
    except TypeError:
        assert d.size() == 0


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_append(iterable):
    '''test the append methood with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    d.append('something')
    assert d.tail.data == 'something'


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_appendleft(iterable):
    '''test the appendleft methood with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    d.appendleft('something')
    assert d.head.data == 'something'


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_appendleft_twice(iterable):
    '''test the appendleft methood with 2 appended values and all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    d.appendleft('something')
    d.appendleft(43)
    assert d.head.data == 43


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_pop(iterable):
    '''test the pop methood with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        d.appendleft('thing')
        assert d.pop() == iterable[0]
    else:
        with pytest.raises(IndexError):
            d.pop()


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_popleft(iterable):
    '''test the pop left with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        assert d.popleft() == iterable[-1]
    else:
        with pytest.raises(IndexError):
            d.popleft()


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_peek(iterable):
    '''test the peek left with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        assert d.peek() == iterable[0]
    else:
        assert d.peek() is None


@pytest.mark.parametrize('iterable', ITERABLE_TABLE)
def test_deque_peekleft(iterable):
    '''test the peekleft left with all values in the ITERABLE_TABLE'''
    from deque import Deque
    d = Deque(iterable)
    if iterable:
        assert d.peekleft() == iterable[-1]
    else:
        assert d.peekleft() is None
