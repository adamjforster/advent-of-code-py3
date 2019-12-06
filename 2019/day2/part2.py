# -*- coding: utf-8 -*-


import operator

from copy import deepcopy


class IntcodeComputer:
    OP_CODES = {
        1: operator.add,
        2: operator.mul,
    }
    
    memory = None
    
    def __init__(self, instructions):
        self.instructions = instructions
        
    def reset(self):
        self.memory = deepcopy(self.instructions)
        
    def run(self, noun, verb):
        self.reset()
        
        self.memory[1] = noun
        self.memory[2] = verb

        # Process code.
        for pointer in range(0, len(self.memory), 4):
            op_code = self.memory[pointer]
    
            if op_code == 99:
                return self.memory[0]
    
            a = self.memory[self.memory[pointer + 1]]
            b = self.memory[self.memory[pointer + 2]]
    
            self.memory[self.memory[pointer + 3]] = IntcodeComputer.OP_CODES[op_code](a, b)


with open('input.txt', 'r') as f:
    code = list(map(int, f.read().split(',')))
    
    computer = IntcodeComputer(code)
    
    for noun in range(0, 99):
        for verb in range(0, 99):
            result = computer.run(noun, verb)
            if result == 19690720:
                print(100 * noun + verb)
