#! /usr/bin/env python3
import os.path

from itertools import pairwise, permutations

from grid import Line, Point, Rectangle, area, rectangle

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


def parse_input(input: list[str]) -> list[Point]:
    return [Point(int(ln.split(",")[0]), int(ln.split(",")[1])) for ln in input]


def part1(input: list[str]):
    red_tiles = parse_input(input)
    red_perms = list(permutations(red_tiles, 2))
    max_area = area(red_perms[0][0], red_perms[0][1])
    max_coord = red_perms[0]
    for candidate in red_perms:
        if area(*candidate) > max_area:
            max_coord = candidate
            max_area = area(*candidate)

    print(f"max_area: {max_area}, co-ordinates: {max_coord}")
    return max_area


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def valid(c1: Point, c2: Point, lines: list[Line], rects: list[Rectangle]) -> bool:
    # given rectangle defined by c1, c2 return true only if the rectangle is within
    # the area described by lines
    #   - every corner must be a point on one of the lines
    #   - or every corner must be "red" that is in one of the rectangles defined by lines
    #
    # note we assume c1 and c2 are valid
    _, _, c3, c4 = rectangle(c1, c2)

    c1_line = False
    c2_line = False
    c3_line = False
    c4_line = False
    c1_rect = False
    c2_rect = False
    c3_rect = False
    c4_rect = False

    for ln in lines:
        if ln.is_on(c1):
            c1_line = True
            break

    for ln in lines:
        if ln.is_on(c2):
            c2_line = True
            break

    for ln in lines:
        if ln.is_on(c3):
            c3_line = True
            break

    for ln in lines:
        if ln.is_on(c4):
            c4_line = True
            break

    for rect in rects:
        if rect.within(c1):
            c1_rect = True
            break

    for rect in rects:
        if rect.within(c2):
            c2_rect = True
            break

    for rect in rects:
        if rect.within(c3):
            c3_rect = True
            break

    for rect in rects:
        if rect.within(c4):
            c4_rect = True
            break

    result = (
        (c1_line or c1_rect)
        and (c2_line or c2_rect)
        and (c3_line or c3_rect)
        and (c4_line or c4_rect)
    )

    print(
        f"{result} - valid({c1}, {c2}, {c3}, {c4} ...) - c1_line: {c1_line}, c2_line: {c2_line}, c3_line: {c3_line}, c4_line: {c4_line}, c1_rect: {c1_rect}, c2_rect: {c2_rect}, c3_rect: {c3_rect}, c4_rect: {c4_rect}"
    )

    return result


def part2(input: list[str]):
    points = parse_input(input)
    rg_zone_points = list(pairwise(points))
    print(rg_zone_points)
    rg_zone_points.append((points[-1], points[0]))
    red_green_zone_lines = [Line(t[0], t[1]) for t in rg_zone_points]
    red_green_zone_rects = [
        Rectangle(t[0], t[1])
        for t in rg_zone_points
        if t[0].r != t[1].r or t[0].c != t[1].c
    ]
    # print(red_green_zone_lines)
    # print(red_green_zone_rects)
    print(
        f"valid((7,3), (11,1), lines) ok: {valid(Point(7, 3), Point(11, 1), red_green_zone_lines, red_green_zone_rects)}"
    )
    print(
        f"valid((9,7), (9,5), lines) ok: {valid(Point(7, 3), Point(11, 1), red_green_zone_lines, red_green_zone_rects)}"
    )
    print(
        f"valid((9,5), (2,3), lines) ok: {valid(Point(9, 5), Point(2, 3), red_green_zone_lines, red_green_zone_rects)}"
    )
    print(
        f"valid((11,1), (2,5), lines) invalid: {valid(Point(11, 1), Point(2, 5), red_green_zone_lines, red_green_zone_rects)}"
    )

    return None


print("test part 2:", part2(test_input))
# print("part 2:", part2(input))
