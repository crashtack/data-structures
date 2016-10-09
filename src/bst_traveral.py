travarsal(add, remove, nonempty)
    while not empty
        curent = remove
        if current is not None:
            yield current.value


class Node(object):

    # pysudo code
    def in_order(self):
        for item in self.left.in_order:
            yeild item
        for item in self.right.in_order:
            yeild item
        yeild self.value
