import pytest


TABLE = [
    ([], []),
    ([0], [0]),
    ([1, 1], [1, 1]),
    ([11, 21], [21, 11]),
    ([11, 21, 3], [21, 11, 3]),
    ([3, 11, 21], [21, 11, 3]),
    ([2, 14, 101, 401, 1000, 401, 501], [1000, 501, 401, 401, 101, 14, 2]),
]


def test_radix():
    '''test that there is a radix sort function'''
    from radix_sort import radix


@pytest.mark.parametrize('init, result', TABLE)
def test_radix_sort(init, result):
    from radix_sort import radix
    sort = radix(init)
    assert sort == result
