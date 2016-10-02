from math import floor


def radix(ll):
    '''radix sort'''
    digit = len(str(max(ll)))
    dict_ = {}
    import pdb; pdb.set_trace()
    while digit:
        for item in ll:
            if digit == 1:
                num = (floor(item / digit) % 10)
            else:
                num = (floor(item / (digit - 1) ** 10) % 10)
