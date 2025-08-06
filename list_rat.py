from collections import deque
def all_rationals() :
    queue = deque([(1,1)])
    while True:
        a,b = queue.popleft()
        yield (a,b)
        queue.append((a, a+b))
        queue.append((a+b,b))