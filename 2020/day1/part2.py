TARGET = 2020


def find_result():
    for i, n in enumerate(numbers):
        for j, o in enumerate(numbers):
            for k, p in enumerate(numbers):
                # Don't add a number to itself.
                if len({i, j, k}) != 3:
                    continue
                
                if n + o + p == TARGET:
                    return n * o * p


with open('input.txt', 'r') as f:
    numbers = [int(n.strip()) for n in f.readlines()]
    result = find_result()
    print(result)
