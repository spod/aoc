#! /usr/bin/env python
import os.path
from collections import defaultdict
test_input = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]


def input_to_graph(input):
    g = defaultdict(list)
    for line in input:
        s, d = line.split('-')
        g[s].append(d)
    return g


def part1(input):
    g = input_to_graph(input)
    print(g)


def part2(input):
    return None


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
