#! /usr/bin/env python3
import os.path

from typing import NamedTuple

from range import Range, merge_ranges

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


class KitchenDB(NamedTuple):
    fresh: list[Range]
    available: list[int]


def parse_input(input: list[str]) -> KitchenDB:
    kdb = KitchenDB([], [])
    ingredients = False
    for line in input:
        if line == "":
            ingredients = True
            continue
        if not ingredients:
            tmp = line.split("-")
            r = Range(int(tmp[0]), int(tmp[1]))
            kdb[0].append(r)
        if ingredients:
            kdb[1].append(int(line))
    return kdb


def part1(input: list[str]):
    kdb = parse_input(input)
    fresh_available: set[int] = set()
    for ingredient in kdb.available:
        if ingredient in fresh_available:
            continue
        for ir in kdb.fresh:
            if ir.contains(ingredient):
                fresh_available.add(ingredient)
                break
    return len(fresh_available)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


# print(f"merge_ranges({parse_input(test_input).fresh}): {merge_ranges(parse_input(test_input).fresh)}")


def part2(input: list[str]):
    kdb = parse_input(input)
    ranges = merge_ranges(kdb.fresh)
    return sum([r.size() for r in ranges])


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
