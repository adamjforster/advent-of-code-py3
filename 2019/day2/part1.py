# -*- coding: utf-8 -*-

import operator


OP_CODES = {
    1: operator.add,
    2: operator.mul,
}


with open('input.txt', 'r') as f:
    code = list(map(int, f.read().split(',')))
    
    # Restore state.
    code[1] = 12
    code[2] = 2
    
    # Process code.
    for position in range(0, len(code), 4):
        op_code = code[position]
        
        if op_code == 99:
            print(code[0])
            exit()
        
        a = code[code[position + 1]]
        b = code[code[position + 2]]
        
        code[code[position + 3]] = OP_CODES[op_code](a, b)

