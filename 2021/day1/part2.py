from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b)
    return zip(a, b)


def tripwise(iterable):
    a, b, c = tee(iterable, 3)
    next(b)
    next(c)
    next(c)
    return zip(a, b, c)


def calculate(depths):
    sums = [sum([a, b, c]) for a, b, c in tripwise(depths)]
    print(sum(1 for a, b in pairwise(sums) if b > a))


with open('input.txt', 'r') as f:
    depths = [int(n.strip()) for n in f.readlines()]
    calculate(depths)
    
        
