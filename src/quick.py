# -*- coding utf-8 -*-
"""Implementation of a quick sort."""
import random

def quick(input_list):
    """Quick sort implementation."""
    if not isinstance(input_list, list):
        raise TypeError

    print('Input List: {}'.format(input_list))
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

    print('Left List: {}'.format(input_list[:left]))
    print('Right List: {}'.format(input_list[left + 1:]))

    input_list[:left] = quick(input_list[:left])
    input_list[left + 1:] = quick(input_list[left + 1:])

    print('End List: {}'.format(input_list))
    return input_list
