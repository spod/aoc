#! /usr/bin/env python
import os.path
from collections import deque
from itertools import islice

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

if "" in test_input:
    test_input.remove("")

# https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable, n):
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def part1(input):
    line = input[0]
    for (p1, p2, p3, p4) in sliding_window(line, 4):
        if len(set([p1, p2, p3, p4])) == 4:
            print(f"signal starts at: {p1}{p2}{p3}{p4}")
            print(line.find("".join([p1, p2, p3, p4])) + 4)
            return line.find("".join([p1, p2, p3, p4])) + 4
    return None


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    line = input[0]
    for chunk in sliding_window(line, 14):
        if len(set(chunk)) == 14:
            schunk = "".join(chunk)
            print(f"signal starts at: {schunk}")
            print(line.find(schunk) + 14)
            return line.find(schunk) + 14
    return None


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
