#! /usr/bin/env python3
import os.path

from typing import NamedTuple, Self

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

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))


class Range:
    min: int
    max: int

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def __lt__(self, other: Self) -> bool:
        return (self.min, self.max) < (other.min, other.max)

    def __repr__(self) -> str:
        return f"Range({self.min},{self.max})"

    def __str__(self) -> str:
        return f"Range({self.min},{self.max})"

    def contains(self, value: int) -> bool:
        return value >= self.min and value <= self.max

    def size(self) -> int:
        return self.max + 1 - self.min


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


def merge_ranges(input: list[Range]) -> list[Range]:
    merged: list[Range] = []
    input.sort()
    merged = [input[0]]
    for rng in input[1:]:
        if merged[-1].max >= rng.min:
            merged[-1] = Range(merged[-1].min, max(merged[-1].max, rng.max))
        else:
            merged.append(rng)
    return merged


# print(f"merge_ranges({parse_input(test_input).fresh}): {merge_ranges(parse_input(test_input).fresh)}")


def part2(input: list[str]):
    kdb = parse_input(input)
    ranges = merge_ranges(kdb.fresh)
    return sum([r.size() for r in ranges])


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
