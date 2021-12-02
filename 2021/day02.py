#! /usr/bin/env python

test_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]
input = list((l.strip() for l in open("./inputs/day02").readlines()))


def partA(input):
    horizontal = 0
    depth = 0
    for move in input:
        (direction, unit) = move.split(' ')
        unit = int(unit)
        # print('direction', direction, 'unit', unit)
        if direction == 'forward':
            horizontal += unit
        elif direction == 'down':
            depth += unit
        elif direction == 'up':
            depth -= unit
        else:
            print("invalid move", move)
    return horizontal * depth


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
    return -42


print("test partB:", partB(test_input))
print("partB:", partB(input))
