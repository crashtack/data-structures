# -*- coding utf-8 -*-
"""Implementation of an insert sort."""

import timeit

def insert(input_list):
    """The insertion sort method."""
    if not isinstance(input_list, list):
        raise TypeError
    
    ordered_list = []

    for index in range(len(input_list)):
        ordered_list.append(input_list[index])
        idx = index
        while idx > 0 and ordered_list[idx] < ordered_list[idx - 1]:
            ordered_list[idx], ordered_list[idx - 1] = ordered_list[idx - 1], ordered_list[idx]
            idx -= 1

    return ordered_list


if __name__ == '__main__':
    time1 = timeit.timeit("insert(best)", setup="from __main__ import insert; best = list(range(100))", number=1000)
    print('''
        BEST CASE:
        The best case senario for the insertion sort method would be were the 
        data is arranged close to the order that you want.  In this case, 
        the algorith will just append and do a check to see if the newly
        appened item is greater than what is in the sorted list, then go onto the
        next item in the input list. Example:
            best = list(range(100))
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time1))

    time2 = timeit.timeit("insert(worst)", setup="from __main__ import insert; worst = list(reversed(list(range(100))))", number=1000)
    print('''
        WORSE CASE:
        The worse case senario would be a list sorted exactly opposite of what 
        you would need.  In this case, the new item woould be appended to
        the list and it would have to be compared and swaped with every
        other member of the sorted list, before the algorith could go onto 
        the next item in the inputted list. Example:
            worse = list(reversed(list(range(100))))
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time2))

    time3 = timeit.timeit("insert(random_list)", setup="from __main__ import insert; import random; random_list = [random.randint(0, 100) for i in range(100)]", number=1000)
    print('''
        RANDOM CASE:
        Example:
            random_list = [random.randint(0, 100) for i in range(100)]
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time3))


