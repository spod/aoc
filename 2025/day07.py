#! /usr/bin/env python3
import os.path

from collections import defaultdict

from grid import build_grid

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


def part1(input: list[str]):
    grid = build_grid(input)
    # grid.print()
    (max_r, _) = grid.size()

    splits = 0
    beams: list[int] = []
    # find start point in first row
    beams.append(grid.row_values(0).index("S"))

    for r in range(1, max_r + 1):
        new_beams: set[int] = set()
        row = grid.row_values(r)
        for b in beams:
            if row[b] == ".":
                new_beams.add(b)
                continue
            if row[b] == "^":
                splits += 1
                new_beams.add(b - 1)
                new_beams.add(b + 1)
        beams = list(new_beams)
    return splits


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input: list[str]):
    grid = build_grid(input)
    (max_r, _) = grid.size()

    beams: list[int] = []
    beam_counts: defaultdict[int, int] = defaultdict(int)
    beams.append(grid.row_values(0).index("S"))
    beam_counts[beams[0]] += 1
    for r in range(1, max_r + 1):
        new_beams: set[int] = set()
        row = grid.row_values(r)
        for b in beams:
            if row[b] == ".":
                new_beams.add(b)
                continue
            if row[b] == "^":
                new_beams.add(b - 1)
                new_beams.add(b + 1)
                count = beam_counts[b]
                if count > 0:
                    beam_counts[b - 1] += count
                    beam_counts[b + 1] += count
                    beam_counts[b] = 0
        beams = list(new_beams)
    return sum(beam_counts.values())


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
