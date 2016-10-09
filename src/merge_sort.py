# -*- coding utf-8 -*-

import timeit

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

def worse_case(my_list=list(range(100))):
    """
    This function is to create a list that is the worse case sort
    for the merge sort method."""
    if len(my_list) == 2:
        my_list[0], my_list[1] = my_list[1], my_list[0]
        return my_list
    elif len(my_list) == 1:
        return my_list
    left = worse_case([i for i in my_list if my_list.index(i) % 2 == 0])
    right = worse_case([i for i in my_list if my_list.index(i) % 2 == 1])

    return left + right


if __name__ == '__main__':
    time1 = timeit.timeit("merge_sort(best)", setup="from __main__ import merge_sort; best = list(range(100))", number=1000)
    print('''
        BEST CASE:
        The best case senario for the merge_sort sort method would be were the 
        data is arranged close to the order that you want.  In this senario,
        when merging the lists back together the sort will do minimal cheecks,
        once the sub-list of smaller values are exahusted, then the remaining
        list can be appeneded without further checks.
        Example:
            best = list(range(100))
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time1))

    time2 = timeit.timeit("merge_sort(worst)", setup="from __main__ import merge_sort; worst = " + str(worse_case()), number=1000)
    print('''
        WORSE CASE:
        The worse case senario would be a list sorted so at each itteration
        the sort would have to do as many checks as posible.  This entails
        breaking apart the list in a specific way, swaping values and building
        the list back-up.  
         Example:
            to sort the worse case senario list 1000 times it took: {0:.5f} sec.
        '''.format(time2))

    time3 = timeit.timeit("merge_sort(random_list)", setup="from __main__ import merge_sort; import random; random_list = range(100); random.shuffle(random_list)", number=1000)
    print('''
        RANDOM CASE:
        Example:
            random_list = [random.randint(0, 100) for i in range(100)]
            to sort this list 1000 times it took: {0:.5f} sec.
        '''.format(time3))

