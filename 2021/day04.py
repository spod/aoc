#! /usr/bin/env python

import os.path
test_input = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7"
]


def read_bingo_boards(input):
    draw_numbers = []
    boards = []

    draw_numbers = [int(x) for x in "\n".join(input).split("\n")[0].split(",")]

    # always 5 x 5 board so read 5 non empty lines at a time into b
    # add b once it's "full" and reset and keep reading input
    b = []
    for line in "\n".join(input).split("\n")[1:]:
        if line != "":
            b.append([int(x) for x in line.split()])
        if b != [] and len(b) == 5:
            boards.append(b)
            b = []

    return (draw_numbers, boards)


def score_card():
    return [[False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
            ]

def bingo_board(b):
    for r in range(5):
        if b[r][0] and b[r][1] and b[r][2] and b[r][3] and b[r][4]:
            return True
    for c in range(5):
        if b[0][c] and b[1][c] and b[2][c] and b[3][c] and b[4][c]:
            return True
    return False

def update_score_board(b, s, n):
    for r in range(5):
        for c in range(5):
            if b[r][c] == n:
                s[r][c] = True
                return s
    return s

def calculate_board_points(b, s):
    sums = 0
    for r in range(5):
        for c in range(5):
            if not s[r][c]:
                sums += b[r][c]
            #print(f"r: {r}, c: {c}, b[r][c]: {b[r][c]}, s[r][c]: {s[r][c]}, sums: {sums}")

    return sums * 24


def pb(b):
    for r in range(5):
        print(" ".join([str(x) for x in b[r]]))

def part1(input):
    # board is 5 x 5 [[n, n, n, n, n], ... ]
    # need to score board [[true, false, true, false, true]]
    # 5 in a row or column wins board
    # Once we have winning board then sum all false and multiple by 24 to get score
    # input has many boards (> 10)
    draw_numbers, boards = read_bingo_boards(input)
    scores = [score_card() for _ in range(len(boards))]

    for draw in draw_numbers:
        for b in range(len(boards)):
            scores[b] = update_score_board(boards[b], scores[b], draw)
            if bingo_board(scores[b]):
                print("Winner!")
                print("Last number drawn: ", draw)
                print("All draw numbers:", draw_numbers)
                print()
                print("Winning board #:", b)
                pb(boards[b])
                pb(scores[b])
                print("score -", calculate_board_points(boards[b], scores[b]))

                print("All boards: ...")
                for brd in range(len(boards)):
                    print(f"board: {brd}")
                    pb(boards[brd])
                    pb(scores[brd])
                    print(f"bingo: {bingo_board(scores[brd])}")
                    print()
                return calculate_board_points(boards[b], scores[b])
    return None


def part2(input):
    return None

# test
# print(bingo_board(score_card()))
# print(bingo_board([[False, False, False, False, False],
#         [False, False, False, False, False],
#         [False, False, False, False, False],
#         [False, False, False, False, False],
#         [True, True, True, True, True]
#         ]))
# print(bingo_board([[True, False, False, False, False],
#         [True, False, False, False, False],
#         [True, False, False, False, False],
#         [True, False, False, False, False],
#         [True, False, False, False, False]
#         ]))

# wb = [
#     [60, 84, 55, 19, 47],
#     [97, 18, 44, 52, 88],
#     [50, 0, 29, 36, 58],
#     [77, 65, 21, 49, 40],
#     [87, 39, 89, 31, 27]
# ]

# ws = [
# [False, True, False, False, False],
# [False, True, True, False, True],
# [False, True, False, False, False],
# [False, True, False, False, False],
# [False, True, True, False, False]
# ]
# print(calculate_board_points(wb,ws))
# import sys; sys.exit(0)

day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print()
print("part 1:", part1(input))
# print("test part 2:", part2(test_input))
# print("part 2:", part2(input))
