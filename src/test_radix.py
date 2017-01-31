import pytest
import random


def create_random(num_elemets):
    """generates a list of random ints, and the sorted list"""
    l1 = []
    for i in range(num_elemets):
        l1.append(random.randint(1, 100))
    return l1, sorted(l1)

TABLE = [
    ([], []),
    ([0], [0]),
    ([1, 1], [1, 1]),
    ([11, 21], [11, 21]),
    ([11, 21, 3], [3, 11, 21]),
    ([3, 11, 21], [3, 11, 21]),
    ([4, 401, 401, 1, 401, 2, 401], [1, 2, 4, 401, 401, 401, 401]),
    ([2, 14, 101, 401, 1000, 401, 501], [2, 14, 101, 401, 401, 501, 1000]),
    (create_random(1000)),
]


def test_radix():
    """test that there is a radix sort function"""
    from radix_sort import radix


@pytest.mark.parametrize('init, result', TABLE)
def test_radix_sort(init, result):
    """test the output of radix sort"""
    from radix_sort import radix
    sort = radix(init)
    assert sort == result
