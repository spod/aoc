#! /usr/bin/env python3
import os.path

from grid import Point, build_grid

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


def part1(input: list[str]):
    grid = build_grid(input)
    (max_r, max_c) = grid.size()
    accessible_rolls: list[Point] = []
    for r in range(0, max_r + 1):
        for c in range(0, max_c + 1):
            cc = Point(r, c)
            # this line took so long to figure out, read spec carefully
            if grid.get_value_at(cc) == "@":
                neighbours = grid.adj_point_values(cc)
                if neighbours.count("@") < 4:
                    accessible_rolls.append(cc)
    return len(accessible_rolls)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input: list[str]):
    grid = build_grid(input)
    (max_r, max_c) = grid.size()

    removed_rolls: list[Point] = []
    removed_last = 1

    while removed_last != 0:
        accessible_rolls: list[Point] = []
        for r in range(0, max_r + 1):
            for c in range(0, max_c + 1):
                cc = Point(r, c)
                if grid.get_value_at(cc) == "@":
                    neighbours = grid.adj_point_values(cc)
                    if neighbours.count("@") < 4:
                        grid.set_value_at(cc, ".")
                        accessible_rolls.append(cc)
        removed_rolls.extend(accessible_rolls)
        removed_last = len(accessible_rolls)
    return len(removed_rolls)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
