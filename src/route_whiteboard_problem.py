import Queue


def valid(root, val):
    rl = []
    c = root
    total = 0
    while c:
        total += c.value
        rl.append(c)
        c = c.parent
        if total == val:
            yield tuple(rl)


def bf(root, val):
    route = []
    c = root
    q = Queue()
    q.enqueue(c)
    while q.size():
        for i in valid(c, val):
            route.append(i)
        if c.left:
            q.enqueue(c.left)
        if c.right:
            q.enqueue(c.right)
        c = q.deque()
    return route
