# -*- coding utf-8 -*-
from binheap import Binheap


class Priorityq(Binheap):

    def __init__(self, iterable=None):
        '''Initialise a Priorityq from a list of lists or tuples where the zeroeth 
        element is the priority'''
        if iterable is None:
            self.priorityq = None
        else:
            try:
                self.priorityq = sorted(iterable, key=lambda tup: tup[0])
            except TypeError:
                raise TypeError('please enter a list/tuple of lists/tuples with priority as the first value ')

    def insert(self, item):
        ''' inserts an item into the queue.'''
        if item is None:
            raise ValueError('insert requires a tuple')
        elif self.priorityq is None:
            self.priorityq = [item]
        else:
            print('priorityq 1: {}'.format(self.priorityq))
            head = []
            tail = []
            if item[0] > self.priorityq[-1][0]:
                self.priorityq.append(item)
                print('priorityq 2: {}'.format(self.priorityq))

            elif item[0] < self.priorityq[0][0]:
                self.priorityq = [item] + self.priorityq
                print('priorityq 3: {}'.format(self.priorityq))

            else:
                for i, ex_item in enumerate(self.priorityq):
                    if self.priorityq[i][0] > ex_item[0]:
                        head = self.priorityq[0:i]
                        tail = self.priorityq[i:]
                        print('head: {}'.format(head))
                        print('tail: {}'.format(tail))
                        break
                self.priorityq = head
                print('priorityq 4: {}'.format(self.priorityq))
                self.priorityq.append(item)
                print('priorityq 5: {}'.format(self.priorityq))
                self.priorityq += tail
                print('priorityq 6: {}'.format(self.priorityq))
        print('priorityq 7: {}'.format(self.priorityq))


    def pop(self):
        '''removes the most important item from the queue.'''
        pass

    def peek(self):
        '''returns the most important item without removing it from the queue.'''
        pass
