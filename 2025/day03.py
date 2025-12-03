#! /usr/bin/env python3
import os.path

from itertools import combinations

day = os.path.basename(__file__).split('.')[0][-2:]
print(f"Day {day}")

test_input_raw = \
"""987654321111111
811111111111119
234234234234278
818181911112111
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

def max_joltage(bank: str, cells: int):
    cell_combos = list(combinations([int(c) for c in bank], cells))
    max_pair = cell_combos[0]
    for p in cell_combos:
        if p > max_pair:
            max_pair = p
    result: list[str] = []
    for v in max_pair:
        result.append(str(v))
    return int("".join(result))

test_values = [("987654321111111", 98),
               ("811111111111119", 89),
               ("234234234234278", 78),
               ("818181911112111", 92)]

# for tc in test_values:
#     print(f"max_joltage({tc[0]}, 2) = {max_joltage(tc[0], 2)}, expected {tc[1]}")

def part1(input: list[str]):
    results: list[int] = []
    for bank in input:
        results.append(max_joltage(bank, 2))
    return sum(results)

print("test part 1:", part1(test_input))
print("part 1:", part1(input))

def part2(input: list[str]):
    results :list[int] = []
    for bank in input:
        results.append(max_joltage(bank, 12))
    return sum(results)

print("test part 2:", part2(test_input))
print("part 2:", part2(input))