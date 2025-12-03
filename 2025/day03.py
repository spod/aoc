#! /usr/bin/env python3
import os.path

from itertools import combinations

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """987654321111111
811111111111119
234234234234278
818181911112111
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))


def _max_joltage_old(bank: str, cells: int):  # type: ignore
    cell_combos = list(set(combinations([int(c) for c in bank], cells)))
    max_pair = cell_combos[0]
    for p in cell_combos:
        if p > max_pair:
            max_pair = p
    result: list[str] = []
    for v in max_pair:
        result.append(str(v))
    return int("".join(result))


def max_joltage(bank: str, cells: int) -> int:
    # 234234234234278, 15, we need 12
    # pick highest cell that allows us to pick remaining cells we need
    # skip 23, choose 4, left with 234234234278
    # have '4' (1), need 11, skip 2, choose 3, left with 4234234278 (10)
    # have '43' + '4234234278'
    bank_jolts = [int(j) for j in bank]
    picked: list[int] = []
    need = cells
    idx = -1
    while need > 0:
        # for 234234234234278, need 12
        # bank_jolts = [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]
        # search_range = bank_jolts[0 : 15 - 12 + 1] = bank_jolts[0:4] = [2, 3, 4, 2], pick = 4, rest = [4, 2, 3, 4, 2, 3, 4, 2, 7, 8], next idx = 2, need = 11
        # search_range = bank_jolts[3 : 15 - 11 + 1] = bank_jolts[3:5] = [2, 3], pick = 3, rest = [2, 3, 4, 2, 3, 4, 2, 7, 8]], next idx = 4, need = 10
        search_range = bank_jolts[idx + 1 : len(bank) - need + 1]
        pick = max(search_range)
        idx = bank_jolts.index(pick, idx + 1)
        picked.append(pick)
        need -= 1
    return int("".join([str(c) for c in picked]))


test_values = [
    ("987654321111111", 2, 98),
    ("811111111111119", 2, 89),
    ("234234234234278", 2, 78),
    ("818181911112111", 2, 92),
    ("987654321111111", 12, 987654321111),
    ("811111111111119", 12, 811111111119),
    ("234234234234278", 12, 434234234278),
    ("818181911112111", 12, 888911112111),
]

# for tc in test_values:
#     print(
#         f"max_joltage({tc[0]}, {tc[1]}) = {max_joltage(tc[0], tc[1])}, expected {tc[2]}"
#     )


def part1(input: list[str]):
    results: list[int] = []
    for bank in input:
        results.append(max_joltage(bank, 2))
    return sum(results)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input: list[str]):
    results: list[int] = []
    for bank in input:
        results.append(max_joltage(bank, 12))
    return sum(results)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
