# -*- coding utf-8 -*-
import pytest
import random
from collections import deque

def merge_sort(input_list):
    if not isinstance(input_list, list):
        raise TypeError

    if len(input_list) <= 1:
        return input_list

    list_length = len(input_list)
    mid = list_length // 2
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left, right):
    ordered_list = []
    i = 0
    j = 0
    while i + j < len(left) + len(right):
        if left[i] <= right[j]:
            ordered_list.append(left[i])
            i += 1
            if i >= len(left):
                ordered_list.extend(right[j:])
                break
        else:
            ordered_list.append(right[j])
            j += 1
            if j >= len(right):
                ordered_list.extend(left[i:])
                break
    return ordered_list
