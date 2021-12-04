#! /usr/bin/env python

import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
test_input = []
input = list((int(l.strip()) for l in open(f"./inputs/day{day}").readlines()))


def part1(input):
    return None


def part2(input):
    return None


print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))