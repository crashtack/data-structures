travarsal(add, remove, nonempty)
    while not empty
        curent = remove
        if current is not None:
            yield current.value


class Node(object):

    
    def in_order(self):
        for item in self.left.in_order:
            yeild item
        for itme in self.right.in_order:
            yeild item
        yeild self.value
