#! /usr/bin/env python
import os.path

from itertools import islice

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

PRI = {}
for ch in range(ord("a"), ord("z") + 1):
    PRI[chr(ch)] = ch - ord("a") + 1
for ch in range(ord("A"), ord("Z") + 1):
    PRI[chr(ch)] = ch - ord("A") + 27


def part1(input):
    total = 0
    for line in input:
        if line != "":
            (l, r) = (line[: int(len(line) / 2)], line[int(len(line) / 2) :])
            (sl, sr) = (set([*l]), set([*r]))
            total += PRI[(sl & sr).pop()]
    return total


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


# From https://docs.python.org/3/library/itertools.html#itertools-recipes
def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch


def part2(input):
    total = 0
    if "" in input:
        input.remove("")
    for batch in batched(input, 3):
        badge = (set([*batch[0]]) & set([*batch[1]]) & set([*batch[2]])).pop()
        total += PRI[badge]
    return total


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
