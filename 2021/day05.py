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
    # pg(grid)
    result = 0
    for xs in grid.values():
        result += len(list(filter(lambda i: i >= 2, list(xs.values()))))
    return result


def pg(grid):
    # this doesn't draw the grid "correctly"
    # cartesian style with (0,0) in bottom left
    # it just prints the backing dictionary!
    Xmin = min(list(grid.keys()))
    Xmax = max(list(grid.keys()))
    Ymin = min(list(grid[Xmin].keys()))
    Ymax = max(list(grid[Xmin].keys()))

    disp = []
    for x in range(Xmin, Xmax + 1):
        disp.append([])
        for y in range(Xmin, Ymax + 1):
            if grid[x].get(y, 0) >= 1:
                disp[x].append(f"{grid[x][y]}")
            else:
                disp[x].append('.')
    for l in disp:
        print("".join(l))


def part2(input):
    # number of points where lines overlap on input
    grid = defaultdict(dict)
    for line in input:
        (x1, y1, x2, y2) = parse_line(line)

        xstep, ystep = 1, 1
        if x1 > x2:
            xstep = -1
        if y1 > y2:
            ystep = -1

        if (x1 == x2) or (y1 == y2):
            for x in range(x1, x2 + xstep, xstep):
                for y in range(y1, y2 + ystep, ystep):
                    grid[x][y] = grid.get(x, {}).get(y, 0) + 1
        else:
            y = y1
            for x in range(x1, x2 + xstep, xstep):
                grid[x][y] = grid.get(x, {}).get(y, 0) + 1
                y = y + ystep

    result = 0
    for xs in grid.values():
        result += len(list(filter(lambda i: i >= 2, list(xs.values()))))
    return result


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
