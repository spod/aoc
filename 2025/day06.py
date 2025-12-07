#! /usr/bin/env python3
import os.path

from collections import defaultdict
from functools import reduce

from grid import *

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))

raw_test_input = list(ln for ln in test_input_raw.splitlines())
raw_input = list((ln.rstrip() for ln in open(f"./inputs/day{day}").readlines()))
if "" in raw_test_input:
    raw_test_input.remove("")
if "" in raw_input:
    raw_input.remove("")


def fadd(x: int, y: int) -> int:
    return x + y


def fmul(x: int, y: int) -> int:
    return x * y


def part1(input: list[str]):
    n_cols = len(input[0].split())
    n_rows = len(input)
    operators = input[-1].split()
    columns: dict[int, list[int]] = defaultdict(list[int])
    for nrow in range(n_rows - 1):
        row = input[nrow]
        tmp_l = row.split()
        tmpi_d = {k: int(tmp_l[k]) for k in range(n_cols)}
        for c in range(n_cols):
            columns[c].append(tmpi_d[c])

    results: list[int] = []

    for col in range(n_cols):
        if operators[col] == "+":
            results.append(reduce(fadd, columns[col]))
        elif operators[col] == "*":
            results.append(reduce(fmul, columns[col]))
    # print(f"#rows: {n_rows}, #columns: {n_cols}")  # , results: {results}")
    return sum(results)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))

print()


def solve_problem(g: Grid, operator: str) -> int:
    results: list[int] = []
    (_, max_c) = g.size()
    for c in range(max_c, -1, -1):
        results.append(int("".join([v for v in g.col_values(c)])))
    if operator == "*":
        return reduce(fmul, results)
    return sum(results)


def part2(input: list[str]):
    grid = build_grid(input[:-1])
    operators = input[-1].split()
    (max_r, max_c) = grid.size()

    # find separators that split problems (an entire column of ' 's)
    separators: list[int] = []
    for c in range(max_c):
        if len(set(grid.col_values(c))) == 1 and grid.col_values(c)[0] == " ":
            separators.append(c)

    # build a list of problems, which are sub grids of overall grid divided by separators
    problems: list[Grid] = []
    start_c = 0
    for sep in separators:
        prob = sub_grid(grid, Point(0, start_c), Point(max_r, sep - 1))
        problems.append(prob)
        start_c = sep + 1
    # last problem is between last separator and end of grid
    last_prob = sub_grid(grid, Point(0, start_c), Point(max_r, max_c))
    problems.append(last_prob)

    results: list[int] = []
    k = 0
    for prob in problems:
        results.append(solve_problem(prob, operators[k]))
        k += 1
    return sum(results)


print("test part 2:", part2(raw_test_input))
print("part 2:", part2(raw_input))
