# -*- coding: utf-8 -*-


def calculate_fuel_for_mass(mass):
    return mass // 3 - 2


def calculate_fuel_for_fuel(fuel_mass):
    new_fuel = calculate_fuel_for_mass(fuel_mass)
    if new_fuel > 0:
        fuel_mass += calculate_fuel_for_fuel(new_fuel)
    return fuel_mass


with open('input.txt', 'r') as f:
    print(sum(calculate_fuel_for_fuel(calculate_fuel_for_mass(int(mass))) for mass in f))
