#! /usr/bin/env python

import os.path
test_input = [
    "3,4,3,1,2"
]


def simulate(sea, days):
    day = 0

    # state value, count of fish
    ocean = dict(zip(range(0, 8 + 1), [0 for _ in range(8 + 1)]))
    for fish in sea:
        ocean[fish] += 1

    while day < days:
        day += 1
        oceanCopy = ocean.copy()
        ocean = dict(zip(range(0, 8 + 1), [0 for _ in range(8 + 1)]))
        for fishState, count in oceanCopy.items():
            if fishState == 0:
                ocean[6] += count
                ocean[8] += count
            else:
                ocean[fishState - 1] += count

        # print(day, sum(ocean.values()), ocean)

    return sum(ocean.values())


def part1(input):
    sea = [int(x) for x in input[0].split(',')]
    return simulate(sea, 80)


def part2(input):
    sea = [int(x) for x in input[0].split(',')]
    return simulate(sea, 256)


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
