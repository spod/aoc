#! /usr/bin/env python3
import os.path

day = os.path.basename(__file__).split('.')[0][-2:]

test_input_raw = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
test_input = list(l.strip() for l in test_input_raw.splitlines())
test_input.remove("")
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))


def partA(input: list[str]):
    curr = 50
    zeroPoints = 0
    for line in input:
        (direction, amount) = (line[0], int(line[1:]))            
        if direction == "L":
            curr = (curr - amount) % 100
        if direction == "R":
            curr = (curr + amount) % 100
        if curr == 0:
            zeroPoints += 1
    return zeroPoints


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input: list[str]):
    position = start = 50
    clicks = 0
    for line in input:
        (direction, amount) = (line[0], int(line[1:]))            
        if direction == "L":
            position -= amount
        if direction == "R":
            position += amount
        extra, position = divmod(position, 100)
        count = int(abs(extra))
        # L end on zero, add 1
        if direction == "L" and position == 0:
            count += 1
        # L start on zero, sub 1
        if direction == "L" and start == 0:
            count -= 1
        clicks += count
        start = position
    return clicks

print("test partB:", partB(test_input))
print("partB:", partB(input))
