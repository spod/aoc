#! /usr/bin/env python
import os.path

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

if "" in test_input:
    test_input.remove("")

if "" in input:
    input.remove("")


def pl(line):
    l, r = line.split(",")
    (lmin, lmax), (rmin, rmax) = l.split("-"), r.split("-")
    lmin, lmax, rmin, rmax = int(lmin), int(lmax), int(rmin), int(rmax)
    return (set(range(lmin, lmax + 1)), set(range(rmin, rmax + 1)))


def part1(input):
    return len(list(filter(lambda t: t[0].issubset(t[1]) or t[1].issubset(t[0]),
                           map(pl, input))))


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    return len(list(filter(lambda t: t[0] & t[1], map(pl, input))))


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
