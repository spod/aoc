#! /usr/bin/env python

test_input = [
    "16,1,2,0,4,2,7,1,2,14"
]


def part1(input):
    crabs = [int(x) for x in input[0].split(',')]
    minFuelCost = None
    for pos in range(min(crabs), max(crabs) + 1):
        cost = fuel_cost(crabs, pos)
        if minFuelCost == None or cost < minFuelCost:
            minFuelCost = cost
    return minFuelCost


def fuel_cost(crabs, target_position, linear=True):
    fuel = 0
    for crab in crabs:
        if linear:
            fuel += abs(crab - target_position)
        else:
            # Triangular numbers!
            # 1 + 2 + 3 + 4 ...
            n = abs(crab - target_position)
            fuel += int((n * (n + 1)) / 2)
    return fuel


def part2(input):
    crabs = [int(x) for x in input[0].split(',')]
    minFuelCost = None
    for pos in range(min(crabs), max(crabs) + 1):
        cost = fuel_cost(crabs, pos, False)
        if minFuelCost == None or cost < minFuelCost:
            minFuelCost = cost
    return minFuelCost


import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
