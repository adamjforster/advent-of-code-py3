import re


PATTERN = r'^(?=.*byr:(19[2-9]\d|200[0-2]))(?=.*iyr:(201\d|2020))(?=.*eyr:(202\d|2030))(?=.*hgt:(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in))(?=.*hcl:(#[a-f\d]{6}))(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))(?=.*pid:\d{9}).*$'


with open('input.txt', 'r') as f:
    num_valid = 0
    for passport in f.read().split('\n\n'):
        passport = passport.replace('\n', ' ')
        if re.match(PATTERN, passport):
            num_valid += 1
    print(num_valid)


# For some reason this gave the result of 225 when the valid answer is
# 224. I'm not sure why.
