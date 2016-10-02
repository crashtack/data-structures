import pytest


TABLE = [
    ([21, 11], [11, 21]),
    ([11, 21, 3], [3, 11, 21]),
]


def test_radix():
    '''test that there is a radix sort function'''
    from radix_sort import radix


@pytest.mark.parametrize('init, result', TABLE)
def test_radix_sort(init, result):
    from radix_sort import radix
    sort = radix(init)
    assert sort == result
