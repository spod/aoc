#! /usr/bin/env python

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
                neighbors.append((r+x,c+y))
    return neighbors


def step_grid(g):
    # increment each level

    for r in range(len(g)):
        for c in range(len(g)):
            g[r][c] += 1
    
    # track which octopus flashed
    flashed = set()
    neighbors_flashed = set()
    f = [ [ False for _ in range(len(g))] for _ in range(len(g))]
    for r in range(len(g)):
        for c in range(len(g)):
            if g[r][c] == 10:
                g[r][c] = 0
                flashed.add((r,c))
                f[r][c] = True

    # now do any follow up flashes based on neighbors incremented
    # until we stop flashing additional cells

    # print("step ... increment only")
    # print(f"flashed: {len(flashed)}, {flashed}")
    # pg(g)

    extra_flashed = -1
    while extra_flashed != 0:
        extra_flashed = 0
        for (r, c) in list(flashed):
            if (r, c) not in neighbors_flashed:
                to_bump = neighbors(r, c, len(g[0]) - 1)
                for (rr, cc) in to_bump:
                    if (rr, cc) not in flashed:
                        g[rr][cc] += 1
                neighbors_flashed.add((r,c))
        for r in range(len(g)):
            for c in range(len(g)):
                if g[r][c] >= 10:
                    g[r][c] = 0
                    if not f[r][c]:
                        f[r][c] = True
                        flashed.add((r,c))
                        extra_flashed += 1

    # print("step ... extra flashes")
    # print(f"flashed: {len(flashed)}, {flashed}")
    # pg(g)
    # print("total flashed this step:", len(flashed))

    pgf(g, flashed)

    return g, len(flashed)

def pg(g):
    for r in g:
        print(" ".join([str(c) for c in r]))

def pgf(g, f):
    print()
    for r in range(len(g)):
        to_print = []
        for c in range(len(g)):
            if (r,c) in f:
                to_print.append(f"\u001b[1m{g[r][c]}\u001b[0m")
            else:
                to_print.append(f"{g[r][c]}")
        print(" ".join(to_print))
            
tg = [
    "11111",
    "19991",
    "19191",
    "19991",
    "11111"
]
g = read_octopus_grid(tg)
print("test grid:")
pg(g)
g, f = step_grid(g)
print()
print("flashed:", f)
print()
g, f = step_grid(g)
print()
pg(g)
print("flashed:", f)
print()

def part1(input):
    steps = 100
    flashes = 0
    g = read_octopus_grid(input)
    pg(g)
    for s in range(steps):
        # print(f"step {s}")
        g, f = step_grid(g)
        flashes += f

    return flashes


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