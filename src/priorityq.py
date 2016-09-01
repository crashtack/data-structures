# -*- coding utf-8 -*-


class Priorityq(object):

    def __init__(self, iterable=None):
        '''Initialise a Priorityq from a list of lists or tuples
            where the zeroeth element is the priority'''
        if iterable is None:
            self.priorityq = None
        else:
            try:
                self.priorityq = sorted(iterable, key=lambda tup: tup[0])
            except TypeError:
                raise TypeError('please enter a list/tuple of '
                                'lists/tuples with priority as '
                                'the first value')

    def insert(self, item):
        ''' inserts an item into the queue.'''
        if item is None:
            raise ValueError('insert requires a tuple')
        elif self.priorityq is None:
            self.priorityq = [item]
        else:
            self.priorityq.append(item)
            self.priorityq = sorted(self.priorityq, key=lambda tup: tup[0])

    def pop(self):
        '''removes the most important item from the queue.'''
        if self.priorityq is None:
            raise IndexError('tried to pop from an empty queue')
        return self.priorityq.pop(0)

    def peek(self):
        '''returns the most important item without removing it
        from the queue.'''
        if self.priorityq is None:
            raise IndexError('tried to peek from an empty queue')
        else:
            return self.priorityq[0]
