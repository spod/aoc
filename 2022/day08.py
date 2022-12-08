#! /usr/bin/env python
import os.path

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
30373
25512
65332
33549
35390
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

if "" in test_input:
    test_input.remove("")
if "" in input:
    input.remove("")


def read_grid(input):
    g = []
    for line in input:
        g.append([int(p) for p in line])
    return g


def pg(g):
    for r in g:
        print(" ".join([str(c) for c in r]))


def visible(g, r, c):
    maxR = len(g[0]) - 1
    maxC = len(g) - 1
    myHeight = g[r][c]

    if r == 0 or c == 0 or r == maxR or c == maxC:
        return True  # edge

    # up
    upVisible = True
    for kr in range(r - 1, 0 - 1, -1):
        upVisible = g[kr][c] < myHeight
        if not upVisible:
            break

    # left
    leftVisible = True
    for kc in range(c - 1, 0 - 1, -1):
        leftVisible = g[r][kc] < myHeight
        if not leftVisible:
            break

    # down
    downVisible = True
    for kr in range(r + 1, maxR + 1):
        downVisible = g[kr][c] < myHeight
        if not downVisible:
            break

    # right
    rightVisible = True
    for kc in range(c + 1, maxC + 1):
        rightVisible = g[r][kc] < myHeight
        if not rightVisible:
            break
    v = upVisible or leftVisible or downVisible or rightVisible
    return v


def scenic_score(g, r, c):
    maxR = len(g[0]) - 1
    maxC = len(g) - 1
    myHeight = g[r][c]

    # up
    u_score = 0
    upVisible = True
    for kr in range(r - 1, 0 - 1, -1):
        upVisible = g[kr][c] < myHeight
        u_score += 1
        if not upVisible:
            break

    # left
    l_score = 0
    leftVisible = True
    for kc in range(c - 1, 0 - 1, -1):
        leftVisible = g[r][kc] < myHeight
        l_score += 1
        if not leftVisible:
            break

    # down
    d_score = 0
    downVisible = True
    for kr in range(r + 1, maxR + 1):
        downVisible = g[kr][c] < myHeight
        d_score += 1
        if not downVisible:
            break

    # right
    r_score = 0
    rightVisible = True
    for kc in range(c + 1, maxC + 1):
        rightVisible = g[r][kc] < myHeight
        r_score += 1
        if not rightVisible:
            break

    return u_score * d_score * l_score * r_score


def part1(input):
    visibles = []
    g = read_grid(input)
    for r in range(0, len(g[0])):
        for c in range(0, len(g)):
            if visible(g, r, c):
                visibles.append((r, c))
    return len(visibles)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    scores = []
    g = read_grid(input)
    for r in range(0, len(g[0])):
        for c in range(0, len(g)):
            scores.append(scenic_score(g, r, c))
    return max(scores)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
