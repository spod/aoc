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


def unique_window_marker(buffer, window_size):
    for chunk in sliding_window(buffer, window_size):
        if len(set(chunk)) == window_size:
            schunk = "".join(chunk)
            marker = buffer.find(schunk) + window_size
            print(f"signal starts at: {schunk}, marker position:{marker}")
            return marker
    return -1


def part1(input):
    line = input[0]
    return unique_window_marker(line, 4)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    line = input[0]
    return unique_window_marker(line, 14)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
