#! /usr/bin/env python
import os.path
from dataclasses import dataclass
from math import dist

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

test2_input_raw = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
test2_input = list(l.strip() for l in test2_input_raw.splitlines())

input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))


@dataclass
class Loc:

    r: int = 0
    c: int = 0

    def __str__(self):
        return f"({self.r}, {self.c})"

    def tup(self):
        return (self.r, self.c)

    def move(self, direction):
        match direction:
            case "R":
                self.c += 1
            case "L":
                self.c -= 1
            case "U":
                self.r += 1
            case "D":
                self.r -= 1

    def touch(self, other):
        neighbours = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                neighbours.append((self.r + x, self.c + y))
        return other.tup() in neighbours


def parse_input(input):
    moves = []
    if "" in input:
        input.remove("")
    for line in input:
        (direction, count) = line.split()
        count = int(count)
        moves.append((direction, count))
    return moves


TAIL_MOVES = {
        (0, 2): (0, 1),
        (0, -2): (0, -1),
        (2, 0): (1, 0),
        (-2, 0): (-1, 0),
        (1, 2): (1, 1),
        (-1, 2): (-1, 1),
        (1, -2): (1, -1),
        (-1, -2): (-1, -1),
        (2, 1): (1, 1),
        (2, -1): (1, -1),
        (-2, 1): (-1, 1),
        (-2, -1): (-1, -1),
        (2, 2): (1, 1),
        (2, -2): (1, -1),
        (-2, 2): (-1, 1),
        (-2, -2): (-1, -1)
    }

def tail_follow(head, tail, direction):
    # return new tail location
    # if touch horizontal/vertical/diagonal - no move
    if tail.touch(head):
        return tail
    # if head on same row, or column and 2 away, move in direction
    if head.r == tail.r or head.c == tail.c:
        tail.move(direction)
        return tail
    # diagonal
    (nr, nc) = (head.r - tail.r, head.c - tail.c)
    (dr, dc) = TAIL_MOVES[nr, nc]
    tail.r += dr
    tail.c += dc
    return tail


def part1(input):

    head = Loc(0, 0)
    tail = Loc(0, 0)
    tail_locations = set()
    tail_locations.add(tail.tup())

    moves = parse_input(input)

    for (direction, count) in moves:
        for _ in range(0, count):
            head.move(direction)
            tail = tail_follow(head, tail, direction)
            tail_locations.add(tail.tup())

    # print(sorted(list(tail_locations)))
    return len(tail_locations)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))

def pg(g):
    for r in g:
        print("".join([str(c) for c in r]))

def print_rope(rope, rr, rc):
    print([s.tup() for s in rope])
    g = [[] for _ in range(rc + 1)]
    for r in range(rr + 1):
        for _ in range(rc + 1):
            g[r].append(".")
    idx = 9
    for seg in rope[::-1]:
        if idx == 0:
            g[seg.r][seg.c] = "H"
        else:
            g[seg.r][seg.c] = idx
        idx -= 1
    pg(g)

def part2(input):
    rope = [Loc(0,0) for _ in range(10)]
    tail_locations = set()
    tail_locations.add(rope[9].tup())

    moves = parse_input(input)

    for (direction, count) in moves:
        for _ in range(0, count):
            rope[0].move(direction)
            for k in range(1, len(rope)):
                rope[k] = tail_follow(rope[k -1], rope[k], direction)
            tail_locations.add(rope[9].tup())


    print(tail_locations)
    return len(tail_locations)

print("test part 2:", part2(test_input))
print("test part 2 2:", part2(test2_input))
print("part 2:", part2(input))
