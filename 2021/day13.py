#! /usr/bin/env python

import os.path
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['axis', 'value'])
test_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]


def parse_input(input):
    # returns (dots, folds)
    # dots - list of (x,y) tuples
    # folds - ('axis', value)
    dots = []
    folds = []
    for line in input:
        if line[0:11] == 'fold along ':
            (axis, value) = line[11:].split("=")
            folds.append(Line(axis, int(value)))
        elif line == "":
            continue
        else:
            (x, y) = line.split(',')
            dots.append(Point(int(x), int(y)))
    return (dots, folds)


def fold_dots(dots, fold):
    new_dots = set()
    if fold.axis == 'x':
        for d in dots:
            if d.x < fold.value:
                new_dots.add(d)
            else:
                xd = d.x - fold.value
                x = d.x - 2 * xd
                new_dots.add(Point(x, d.y))
    elif fold.axis == 'y':
        for d in dots:
            if d.y < fold.value:
                new_dots.add(d)
            else:
                yd = d.y - fold.value
                y = d.y - 2 * yd
                new_dots.add(Point(d.x, y))
    return list(new_dots)


def print_dots(dots):
    max_x, max_y = 0, 0
    for p in dots:
        if p.x > max_x:
            max_x = p.x
        if p.y > max_y:
            max_y = p.y
    g = [[] for _ in range(max_y + 1)]
    for y in range(max_y + 1):
        for _ in range(max_x + 1):
            g[y].append(' ')
    for p in dots:
        g[p.y][p.x] = '#'
    for l in g:
        print("".join(l))


def part1(input):
    dots, folds = parse_input(input)
    dots = fold_dots(dots, folds[0])
    return len(dots)


def part2(input):
    dots, folds = parse_input(input)
    for fold in folds:
        dots = fold_dots(dots, fold)
    print_dots(dots)


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))
