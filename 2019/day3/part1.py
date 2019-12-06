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
    circuit = defaultdict(lambda: defaultdict(set))
    
    for wire, path in enumerate(f):
        x, y = 0, 0
        
        for instruction in path.split(','):
            direction = instruction[0]
            distance = int(instruction[1:])
            
            if direction in ['L', 'R']:
                new_x = OPS[direction](x, distance)
                step = 1 if new_x > x else -1
                for index in range(x, new_x + step, step):
                    circuit[index][y].add(wire)
                x = new_x
            else:
                new_y = OPS[direction](y, distance)
                step = 1 if new_y > y else -1
                for index in range(y, new_y + step, step):
                    circuit[x][index].add(wire)
                y = new_y
                
    intersections = []
    for row, columns in circuit.items():
        for column, wires in columns.items():
            if row == 0 and column == 0:
                continue

            if len(wires) == 2:
                intersections.append((row, column))

    print(min(abs(intersect[0]) + abs(intersect[1]) for intersect in intersections))
