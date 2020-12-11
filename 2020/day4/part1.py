import re


PATTERN = r'^(?=.*byr:)(?=.*iyr:)(?=.*eyr:)(?=.*hgt:)(?=.*hcl:)(?=.*ecl:)(?=.*pid:).*$'


with open('input.txt', 'r') as f:
    num_valid = 0
    for passport in f.read().split('\n\n'):
        passport = passport.replace('\n', ' ')
        if re.match(PATTERN, passport):
            num_valid += 1
    print(num_valid)
