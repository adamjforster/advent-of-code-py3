TARGET = 2020


def find_result():
    for i, n in enumerate(numbers):
        for j, o in enumerate(numbers):
            # Don't add a number to itself.
            if i == j:
                continue
            
            if n + o == TARGET:
                return n * o


with open('input.txt', 'r') as f:
    numbers = [int(n.strip()) for n in f.readlines()]
    result = find_result()
    print(result)
