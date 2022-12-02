#! /usr/bin/env python
import os.path

from enum import Enum

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
A Y
B X
C Z
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

Result = Enum("Result", ["Win", "Loose", "Draw"])
Move = Enum("Move", ["Rock", "Paper", "Scissors"])

MOVE_SCORE = {
    Move.Rock: 1,
    Move.Paper: 2,
    Move.Scissors: 3,
}

RESULT_SCORE = {
    Result.Loose: 0,
    Result.Draw: 3,
    Result.Win: 6,
}

MOVE_CODE = {
    "A": Move.Rock,
    "B": Move.Paper,
    "C": Move.Scissors,
    "X": Move.Rock,
    "Y": Move.Paper,
    "Z": Move.Scissors,
}

RESULT_CODE = {
    "X": Result.Loose,
    "Y": Result.Draw,
    "Z": Result.Win,
}

RESULTS = {
    Move.Rock: {
        Move.Rock: Result.Draw,
        Move.Paper: Result.Win,
        Move.Scissors: Result.Loose,
    },
    Move.Paper: {
        Move.Rock: Result.Loose,
        Move.Paper: Result.Draw,
        Move.Scissors: Result.Win,
    },
    Move.Scissors: {
        Move.Rock: Result.Win,
        Move.Paper: Result.Loose,
        Move.Scissors: Result.Draw,
    },
}

WIN = {Move.Rock: Move.Paper, Move.Paper: Move.Scissors, Move.Scissors: Move.Rock}

LOOSE = {
    Move.Rock: Move.Scissors,
    Move.Paper: Move.Rock,
    Move.Scissors: Move.Paper,
}


def moves(line):
    (opp, mine) = line.split()
    return (MOVE_CODE[opp], MOVE_CODE[mine])


def part1(input):
    score = 0
    for line in input:
        if line != "":
            (opp, me) = moves(line)
            r = RESULTS[opp][me]
            score += MOVE_SCORE[me]
            score += RESULT_SCORE[r]
    return score


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def parse_game(line):
    (opp, res) = line.split()
    return (MOVE_CODE[opp], RESULT_CODE[res])


def part2(input):
    score = 0
    for line in input:
        if line != "":
            (opp, r) = parse_game(line)
            if r == Result.Draw:
                me = opp
            elif r == Result.Win:
                me = WIN[opp]
            else:
                me = LOOSE[opp]
            score += MOVE_SCORE[me]
            score += RESULT_SCORE[r]
    return score


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
