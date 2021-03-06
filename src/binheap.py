# -*- coding utf-8 -*-


class Binheap(object):

    def __init__(self, iterable=None):
        '''Initialise a heap from an iterable or an empty heap'''
        if iterable is None:
            self.heap = None
        else:
            self.heap = sorted(iterable)

    def push(self, val):
        '''puts new value ito the heap, maintaining the heap property'''
        if val is None:
            raise ValueError('push requires a numeric value')
        elif self.heap is None:
            self.heap = [val]
        else:
            print('heap: {}'.format(self.heap))
            head = []
            tail = []
            if val > self.heap[-1]:
                self.heap.append(val)
            elif val < self.heap[0]:
                self.heap = [val] + self.heap
            else:
                for i, v in enumerate(self.heap):
                    if self.heap[i] > val:
                        head = self.heap[0:i]
                        tail = self.heap[i:]
                        break
                self.heap = head
                self.heap.append(val)
                self.heap += tail

    def pop(self):
        '''rmoves the "top" of the heap, and resorts the heap'''
        if self.heap is None:
            raise IndexError('tried to pop for nothing')
        return self.heap.pop(0)
