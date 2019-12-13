# -*- coding: utf-8 -*-

import operator

from collections import defaultdict


OPS = {
    'L': operator.sub,
    'R': operator.add,
    'U': operator.add,
    'D': operator.sub,
}


with open('input.txt', 'r') as f:
    circuit = defaultdict(lambda: defaultdict(dict))
    
    for wire, path in enumerate(f):
        x, y = 0, 0
        steps = -1  # Don't count the initial step.
        
        for instruction in path.split(','):
            direction = instruction[0]
            distance = int(instruction[1:])
            
            if direction in ['L', 'R']:
                new_x = OPS[direction](x, distance)
                step = 1 if new_x > x else -1
                for index in range(x, new_x + step, step):
                    steps += 1
                    if wire not in circuit[index][y]:
                        circuit[index][y][wire] = steps
                x = new_x
            else:
                new_y = OPS[direction](y, distance)
                step = 1 if new_y > y else -1
                for index in range(y, new_y + step, step):
                    steps += 1
                    if wire not in circuit[x][index]:
                        circuit[x][index][wire] = steps
                y = new_y
            
            # Because of the way we're doing the ranges above we end up
            # with an extra step per instruction, so we remove it here.
            steps -= 1
            
    intersections = []
    for row, columns in circuit.items():
        for column, wire_data in columns.items():
            if row == 0 and column == 0:
                continue

            if len(wire_data.keys()) == 2:
                intersections.append(sum(wire_data.values()))

    print(min(intersections))
