#! /usr/bin/env python

from collections import defaultdict

import os.path
test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
]


def parse_line(line):
    c = [xy.split(",") for xy in line.split(" -> ")]
    return (int(c[0][0]), int(c[0][1]), int(c[1][0]), int(c[1][1]))


def part1(input):
    # number of points where lines overlap on input
    grid = defaultdict(dict)
    for line in input:
        (x1, y1, x2, y2) = parse_line(line)
        # only horizontal / vertical lines
        if (x1 == x2) or (y1 == y2):
            xstep, ystep = 1, 1
            if x1 > x2:
                xstep = -1
            if y1 > y2:
                ystep = -1
            for x in range(x1, x2 + xstep, xstep):
                for y in range(y1, y2 + ystep, ystep):
                    grid[x][y] = grid.get(x, {}).get(y, 0) + 1
    result = 0
    for xs in grid.values():
        result += len(list(filter(lambda i: i >= 2, list(xs.values()))))
    return result


def part2(input):
    return None


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
# print("test part 2:", part2(test_input))
# print("part 2:", part2(input))
