#! /usr/bin/env python

test_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]

def read_points_grid(input):
    g = []
    for line in input:
        g.append([int(p) for p in line])
    # for r in g:
    #     print(r)
    return g

def adjacent(grid, r, c):
    adj = []
    # up
    if r >= 1:
        adj.append(grid[r-1][c])
    # down
    if r < len(grid) - 1:
        adj.append(grid[r+1][c])
    # left
    if c >= 1:
        adj.append(grid[r][c-1])
    # right
    if c < len(grid[0]) - 1:
        adj.append(grid[r][c+1])
    return adj


def part1(input):
    low_points = []
    risk = 0
    g = read_points_grid(input)
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] < min(adjacent(g, r, c)):
                low_points.append((r,c, '-', g[r][c]))
                risk += g[r][c] + 1
    # print()
    # print("\n".join([str(t) for t in low_points]))
    return risk


def part2(input):
    return None


import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
# print("test part 2:", part2(test_input))
# print("part 2:", part2(input))