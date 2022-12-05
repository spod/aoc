#! /usr/bin/env python
import os.path

from collections import defaultdict, namedtuple

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

test_input = list(l for l in test_input_raw.splitlines())
input = list((l for l in open(f"./inputs/day{day}").readlines()))

Move = namedtuple("Move", ["qty", "src", "dst"])


def parse_input(input):
    stacks = defaultdict(list)
    moves = []
    if "" in input:
        input.remove("")
    nStacks = -1
    for line in input:
        if "[" in line:
            if nStacks < 0:
                nStacks = (len(line) + 1) // 4
                print("number of stacks:", nStacks)
            s = 0
            while s < nStacks:
                c = line[1 + 4 * s]
                if c.strip() != "":
                    stacks[s + 1].insert(0, c)
                s += 1
        if "move" in line:
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace("to ", "")
            line = [int(d) for d in line.split()]
            move = Move(*line)
            moves.append(move)
    return (nStacks, stacks, moves)


def part1(input):
    nStacks, stacks, moves = parse_input(input)
    for move in moves:
        q = move.qty
        while q > 0:
            stacks[move.dst].append(stacks[move.src].pop())
            q -= 1
    msg = []
    for s in range(1, nStacks + 1):
        msg.append(stacks[s].pop())
    return "".join(msg)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    nStacks, stacks, moves = parse_input(input)
    for move in moves:
        q = move.qty
        tmp = []
        while q > 0:
            tmp.insert(0, stacks[move.src].pop())
            q -= 1
        stacks[move.dst].extend(tmp)
    msg = []
    for s in range(1, nStacks + 1):
        msg.append(stacks[s].pop())
    return "".join(msg)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
