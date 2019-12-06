# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    print(sum(int(mass) // 3 - 2 for mass in f))
