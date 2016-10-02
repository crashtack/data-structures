from math import floor
from stack import Stack


def radix(l1):
    '''radix sort'''
    digit = len(str(max(l1)))
    dict_ = {}
    # import pdb; pdb.set_trace()
    while digit:
        for i in range(10):
            dict_[i] = Stack()
        # import pdb; pdb.set_trace()

        # load the up dict_
        for item in l1:
            if digit == 1:
                num = (floor(item / digit) % 10)
            else:
                num = (floor(item / (digit - 1) ** 10) % 10)
            dict_[num].push(item)

        # empty the dict_ back into the list
        l1 = []
        for i in range(10):
            while dict_[i].size():
                l1.append(dict_[i].pop())

        digit -= 1
    # import pdb; pdb.set_trace()

    return l1
