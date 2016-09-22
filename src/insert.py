# -*- coding utf-8 -*-
"""Implementation of an insert sort."""

def insert(input_list):
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