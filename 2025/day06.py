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
raw_input = list((ln for ln in open(f"./inputs/day{day}").readlines()))
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


def part2(input: list[str]):
    grid = build_grid(input[:-1], "0")
    operators = input[-1].split()
    (_, max_c) = grid.size()
    grid.print()
    print(f"operators: {operators}")

    for c in range(max_c + 1):
        if sum([int(v) for v in grid.col_values(c)]) == 0:
            print(f"separator column: {c}")


print("test part 2:", part2(raw_test_input))
# print("part 2:", part2(raw_input))
