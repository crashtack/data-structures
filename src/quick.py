# -*- coding utf-8 -*-
"""Implementation of a quick sort."""
import random
import timeit

def quick(input_list):
    """Quick sort implementation."""
    if not isinstance(input_list, list):
        raise TypeError

    if len(input_list) <= 1:
        return input_list

    pivot = input_list[-1]

    if len(input_list) == 2:
        if input_list[0] > pivot:
            input_list[0], input_list[-1] = input_list[-1], input_list[0]
        return input_list

    left = 0
    right = len(input_list) - 2

    while left <= right:
        if input_list[left] < pivot and left <= len(input_list) - 2:
            left += 1
            continue
        if input_list[right] >= pivot and right >= 0:
            right -= 1
            continue
        if input_list[left] > input_list[right]:
            input_list[right], input_list[left] = input_list[left], input_list[right]

    input_list[left], input_list[-1] = input_list[-1], input_list[left]

    input_list[:left] = quick(input_list[:left])
    input_list[left + 1:] = quick(input_list[left + 1:])

    return input_list


def worse_case(my_list=list(range(100))):
    """
    This function is to create a list that is the worse case sort
    for the quick sort method."""
    return [5] * 100

def best_case(my_list=list(range(100))):
    """
    This function is to create a list that is the worse case sort
    for the quick sort method."""
    if len(my_list) <= 1:
        return my_list
    else:
        mid = len(my_list) // 2
        return (
            best_case(my_list[:mid - 1]) +
            best_case(my_list[mid + 1:]) +
            [my_list[mid]]
        )


if __name__ == '__main__':
    time1 = timeit.timeit("quick(best)", setup="from __main__ import quick; best = "+ str(best_case()), number=1000)
    print('''
        BEST CASE:
        The best case senario for the quick sort method would if the list 
        was sorted such that the selectedpivot would be the midpoint of 
        the range. Additionally, each sub-list would also have this
        property.  For our implementation of the last value of the range 
        would be the midpoint of the range of numbers.
        Example:
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time1))

    time2 = timeit.timeit("quick(worst)", setup="from __main__ import quick; worst = " + str(worse_case()), number=1000)
    print('''
        WORSE CASE:
        The worse case senario would be a list that has the same value for
        all of its members.
         Example:
            to sort the worse case senario list 1000 times it took: {0:.5f} sec.
        '''.format(time2))

    time3 = timeit.timeit("quick(random_list)", setup="from __main__ import quick; import random; random_list = [random.randint(0, 100) for i in range(100)]", number=1000)
    print('''
        RANDOM CASE:
        Example:
            random_list = [random.randint(0, 100) for i in range(100)]
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time3))

