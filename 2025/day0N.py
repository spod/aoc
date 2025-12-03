#! /usr/bin/env python3
import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
print(f"Day {day}")

test_input_raw = """
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

def part1(input):
    return None

print("test part 1:", part1(test_input))
print("part 1:", part1(input))

def part2(input):
    return None

print("test part 2:", part2(test_input))
print("part 2:", part2(input))