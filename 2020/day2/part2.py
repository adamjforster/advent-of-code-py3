import re


PATTERN = r'(\d+)-(\d+) (\w): (\w+)'


def count_valid_passwords():
    num_valid = 0
    for line in f.readlines():
        i, j, letter, password = re.match(PATTERN, line).group(1, 2, 3, 4)
        if (password[int(i) - 1] == letter) ^ (password[int(j) - 1] == letter):
            num_valid += 1
            
    return num_valid
    

with open('input.txt', 'r') as f:
    result = count_valid_passwords()
    print(result)
