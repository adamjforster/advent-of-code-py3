# -*- coding: utf-8 -*-

INPUT_RANGE = '278384-824795'
RANGE_START, RANGE_END = INPUT_RANGE.split('-')


def is_password_valid(password):
    has_double = False
    previous = -1
    for digit in str(password):
        digit = int(digit)
        if previous > digit:
            return False
        elif previous == digit:
            has_double = True
        previous = digit
    return has_double
    

valid_passwords = set(
    pwd
    for pwd in range(int(RANGE_START), int(RANGE_END) + 1)
    if is_password_valid(pwd)
)
print(len(valid_passwords))
