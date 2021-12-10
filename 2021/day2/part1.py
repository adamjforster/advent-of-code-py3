import operator


with open('input.txt', 'r') as f:
    axes = {'x': 0, 'y': 0}
    operations = {
        'forward': ('x', operator.add),
        'up': ('y', operator.sub),
        'down': ('y', operator.add)
    }
    
    instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f]
    for direction, amount in instructions:
        axis, op = operations[direction]
        axes[axis] = op(axes[axis], amount)
        
    print(axes['x'] * axes['y'])
