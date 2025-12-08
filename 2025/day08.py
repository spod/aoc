#! /usr/bin/env python3
import os.path

from itertools import permutations
from math import sqrt

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))

class Point:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    # TODO research how to type magic methods like __add__
    def __add__(self, other):  # type: ignore
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)  # type: ignore

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"

def distance(p1: Point, p2: Point) -> float:
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def part1(input: list[str]):
    junction_boxes: list[Point] = []
    distances: dict[float, tuple[Point,Point]] = {}
    for ln in input:
        parts = ln.split(",")
        junction_boxes.append(Point(int(parts[0]), int(parts[1]), int(parts[2])))
    perms = permutations(junction_boxes, 2)
    for perm in perms:
        distances[distance(perm[0], perm[1])] = perm
    ordered_distances = sorted(distances.keys())
    for dist in ordered_distances[0:5]:
        print(dist, distances[dist])
    return None


print("test part 1:", part1(test_input))
import sys;sys.exit()
print("part 1:", part1(input))


def part2(input: list[str]):
    return None


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
