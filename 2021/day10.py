#! /usr/bin/env python

test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]"
]

matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def check_line(line):
    # returns (valid, error_character)
    #  - valid - boolean, true/false
    #  - error_character - if invalid, the first invalid character
    stack = []
    for c in line:
        if c in matches.keys():
            stack.append(c)
        elif c in matches.values():
            l = stack.pop()
            if matches[l] != c:
                return (False, c)
        else:
            print(f"Unexpected {c}")
    return (True, "")

# test check_line ...
#
# test_cases = [
#     ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
#     ("[[<[([]))<([[{}[[()]]]", ")"),
#     ("[{[{({}]{}}([{[{{{}}([]", "]"),
#     ("[<(<(<(<{}))><([]([]()", ")"),
#     ("<{([([[(<>()){}]>(<<{{", ">")
#      ("[({(<(())[]>[[{[]{<()<>>", "") # actually valid so should fail
# ]
#
# for t in test_cases:
#     (v, e) = check_line(t[0])
#     if v:
#         print(f"Error, {t} should fail")
#     else:
#         if e != t[1]:
#             print(f"Error, expected {e}, got {t[1]} for {t[0]}")
#         else:
#             print(f"OK - {t}")

illegal_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def part1(input):
    score = 0
    for line in input:
        (v, e) = check_line(line)
        if not v:
            score += illegal_points[e]
    return score


def part2(input):
    return None


import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
print("part 2:", part2(input))