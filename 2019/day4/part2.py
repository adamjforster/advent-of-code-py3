# -*- coding: utf-8 -*-

from collections import defaultdict


INPUT_RANGE = '278384-824795'
RANGE_START, RANGE_END = INPUT_RANGE.split('-')


def is_password_valid(password):
    doubles = defaultdict(lambda: False)
    double_digit = None
    previous = -1
    
    for digit in str(password):
        digit = int(digit)
        if previous > digit:
            return False
        elif previous == digit:
            if digit == double_digit:
                doubles[digit] = False
            else:
                double_digit = digit
                doubles[digit] = True
        previous = digit
    
    return any(doubles.values())


valid_passwords = set(
    pwd
    for pwd in range(int(RANGE_START), int(RANGE_END) + 1)
    if is_password_valid(pwd)
)
print(len(valid_passwords))
