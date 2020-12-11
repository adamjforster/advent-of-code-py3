TREE = '#'


def solve():
    topography = build_topography()
    max_x = len(topography[0]) - 1
    max_y = len(topography) - 1
    
    num_trees = 0
    
    x = 0
    y = 0
    while y <= max_y:
        if topography[y][x] == TREE:
            num_trees += 1

        x, y = move(x, y, max_x)
    
    return num_trees


def move(x, y, max_x):
    x += 3
    y += 1
    
    if x > max_x:
        x -= max_x + 1
    
    return x, y


def build_topography():
    topography = []
    with open('input.txt', 'r') as f:
        for line in f:
            row = []
            for item in line.strip():
                row.append(item)
            topography.append(row)
                
    return topography


if __name__ == '__main__':
    result = solve()
    print(result)
