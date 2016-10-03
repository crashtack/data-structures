from math import floor
from queue_ import Queue


def radix(l1):
    '''radix sort: start with the least significant bit'''
    try:
        digit = len(str(max(l1)))
    except ValueError:
        print(l1)
        return l1
    dict_ = {}

    for i in range(1, digit + 1):
        for j in range(10):
            dict_[j] = Queue()

        # load the up dict_
        for item in range(len(l1)):
            if digit == 1:
                num = (floor(l1[item] / i) % 10)
            else:
                num = (floor(l1[item] / 10 ** (i - 1)) % 10)
            dict_[num].enqueue(l1[item])

        # empty the dict_ back into the list
        l1 = []
        i = 10
        while i:
            i -= 1
            while dict_[i].size():
                l1.append(dict_[i].dequeue())
    return l1

if __name__ == "__main__":
    import random
    import time

    l3 = []
    for i in range(10000):
        l3.append(i)
    start = time.clock()
    radix(l3)
    interval = time.clock() - start
    print('Best case, an ordered list')
    print("Time: {}sec to sort a 10000 element list of ordered ints from 1 to 10000".format(interval))

    l2 = []
    for i in range(10000):
        l2.append(random.randint(1, 1000))

    start = time.clock()
    radix(l2)
    interval = time.clock() - start
    print('worst case, a random list')
    print("Time: {}sec to sort a 10000 element list of random ints from 1 to 1000".format(interval))

    l4 = []
    for i in range(10000):
        l4.append(1)
    start = time.clock()
    radix(l4)
    interval = time.clock() - start
    # print("Time: {}sec to sort a 10000 element list of ordered ints from 1 to 10000".format(interval))
