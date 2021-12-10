from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b)
    return zip(a, b)


def calculate(depths):
    print(sum(1 for a, b in pairwise(depths) if b > a))


with open('input.txt', 'r') as f:
    depths = [int(n.strip()) for n in f.readlines()]
    calculate(depths)
