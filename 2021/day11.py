#! /usr/bin/env python

import os.path
test_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]

# First, the energy level of each octopus increases by 1.
# Then, any octopus with an energy level greater than 9 flashes.
#  This increases the energy level of all adjacent octopuses by 1,
#  including octopuses that are diagonally adjacent. If this causes
#  an octopus to have an energy level greater than 9, it also flashes.
#  This process continues as long as new octopuses keep having their
#  energy level increased beyond 9.
#  (An octopus can only flash at most once per step.)
# Finally, any octopus that flashed during this step has its energy level
# set to 0, as it used all of its energy to flash.


def read_octopus_grid(input):
    g = []
    for line in input:
        g.append([int(p) for p in line])
    return g


def neighbors(r, c, max_xy):
    neighbors = []
    # all surrounding cells which exist
    min_xy = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if r + x >= min_xy and r + x <= max_xy and c + y >= min_xy and c + y <= max_xy and not (x == 0 and y == 0):
                neighbors.append((r+x, c+y))
    return neighbors


def step_grid(g):
    # increment each level

    for r in range(len(g)):
        for c in range(len(g)):
            g[r][c] += 1

    # track which octopus flashed
    flashed = set()
    neighbors_flashed = set()
    f = [[False for _ in range(len(g))] for _ in range(len(g))]
    for r in range(len(g)):
        for c in range(len(g)):
            if g[r][c] == 10:
                g[r][c] = 0
                flashed.add((r, c))
                f[r][c] = True

    # now do any follow up flashes based on neighbors incremented
    # until we stop flashing additional cells

    # keep looping until we stop flashing extra cells ...
    extra_flashed = -1
    while extra_flashed != 0:
        extra_flashed = 0

        # first bump neighbours for any cells flashed last iteration
        # (and track the ones which were bumped in neighbors_flashed to prevent duplicates)
        for (r, c) in list(flashed):
            if (r, c) not in neighbors_flashed:
                to_bump = neighbors(r, c, len(g[0]) - 1)
                for (rr, cc) in to_bump:
                    if (rr, cc) not in flashed:
                        g[rr][cc] += 1
                neighbors_flashed.add((r, c))
        # now go through grid again to see are were any extra cells flashed
        # if they were add them to flashed (and not neighbors_flashed yet)
        # and increment extra_flashed so we keep looping through to get neighbors on next iteration
        #
        # yes this could be clearer and probably should be recursive, but, it works
        # and gets to a stable state for valid input
        for r in range(len(g)):
            for c in range(len(g)):
                if g[r][c] >= 10:
                    g[r][c] = 0
                    if not f[r][c]:
                        f[r][c] = True
                        flashed.add((r, c))
                        extra_flashed += 1

    # debug print surprisingly useful / pretty
    # pgf(g, flashed)
    return g, len(flashed)


def pg(g):
    for r in g:
        print(" ".join([str(c) for c in r]))


def pgf(g, f):
    print()
    for r in range(len(g)):
        to_print = []
        for c in range(len(g)):
            if (r, c) in f:
                to_print.append(f"\u001b[1m{g[r][c]}\u001b[0m")
            else:
                to_print.append(f"{g[r][c]}")
        print(" ".join(to_print))


def part1(input):
    steps = 100
    flashes = 0
    g = read_octopus_grid(input)
    for s in range(steps):
        g, f = step_grid(g)
        flashes += f

    return flashes


def part2(input):
    g = read_octopus_grid(input)
    all_flashed = False
    s = 0
    gs = len(g) * len(g[0])
    while not all_flashed:
        g, f = step_grid(g)
        s += 1
        all_flashed = gs == f

    return s


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
