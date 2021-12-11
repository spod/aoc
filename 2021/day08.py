#! /usr/bin/env python

import os.path
from collections import defaultdict

single_test_input = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
]
test_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]


digits_to_binary = {
    #    ABCDEFG
    0: 0b1110111,
    1: 0b0010010,
    2: 0b1011101,
    3: 0b1011011,
    4: 0b0111010,
    5: 0b1101011,
    6: 0b1101111,
    7: 0b1010010,
    8: 0b1111111,
    9: 0b1111011
}

digits_to_chrs = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

digits_to_len = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}


def parse_line(line):
    parts = line.split(' | ')
    return (parts[0].split(' '), parts[1].split(' '))


def part1(data):
    uniques = 0
    criteria = [
        digits_to_len[1],
        digits_to_len[4],
        digits_to_len[7],
        digits_to_len[8],
    ]
    for line in data:
        (_, output) = parse_line(line)
        uniques += len(list(filter(lambda x: len(x) in criteria, output)))
    return uniques


def part2(data):
    # Need to figure out decryption key...
    #
    # For (input | output):
    #   acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
    #
    # Based on unique lengths we know:
    #   1, 0b0010010, 'cf'      =>  'ab'
    #   4, 0b0111010, 'bcdf'    =>  'eafb'
    #   7, 0b1011011, 'acf'     =>  'dab'
    #   8, 0b1010010, 'abcdefg' =>  'acedgfb'
    #
    # Need to compute remaining:
    #   0, 'abcefg' => 'cagedb'
    #   2, 'acdeg'  => 'gcdfa'
    #   3, 'acdfg'  => 'fbcad'
    #   5, 'abdfg'  => 'cdfbe'
    #   6, 'abdefg' => 'cdfgeb'
    #   9, 'abcdfg' => 'cefabd'
    #
    # Candidates based on known:
    #  a - [d]
    #  b - [e,f]
    #  c - [a,b]
    #  d - [e,f]
    #  e - [c,g]
    #  f - [a,b]
    #  g - [c,g]
    #
    # Need to keep reducing/guessing further to get key:
    #   'abcdefg' -> 'deafgbc'

    known_lengths = [
        digits_to_len[1],
        digits_to_len[4],
        digits_to_len[7],
        digits_to_len[8],
    ]

    for line in data:

        # substitution from original to scrambled
        key = {}

        # possible candidates that character maps to see example above
        candidates = defaultdict(set)

        num_to_seq = {}
        (input, output) = parse_line(line)
        all_seqs = input.copy()
        all_seqs.extend(output)

        # first figure out initial candidates based on known lengths
        # starting from shortest to longest sequence
        all_seqs.sort(key=len)
        for seq in all_seqs:
            if len(seq) in known_lengths:
                n = [1, 4, 7, 8][known_lengths.index(len(seq))]
                num_to_seq[n] = seq
                for c in digits_to_chrs[n]:
                    if len(candidates[c]) == 0:
                        #print(f"{n}) adding {seq} as candidate for {c}")
                        candidates[c] |= set(list(seq))
        # now figure out the rest!
        # - reduce
        # - once we have reduced, can we match any further sequences to a number?
        # - guess if can't reduce further?
        print("known:", num_to_seq)
        print(f"candidates: {candidates}")
        while reduce(candidates) != candidates:
            candidates = reduce(candidates)
        print(f"reduced candidates: {candidates}")
        for k, v in candidates.items():
            if len(v) == 1:
                key[k] = v.pop()

        to_solve = set(list(range(0, 9+1))) - set(num_to_seq.keys())
        print("To solve:", to_solve)

        print(f"known key: {key}")
    return None

def reduce(candidates):
    # - reduce
    #   - if candidate set is a superset of smaller sets for other candidates
    #     then we can remove the smaller set from this candidate set ...
    #        eg. 'a': {'b', 'a', 'd'}
    #            'c': {'b', 'a'}
    #            'f': {'b', 'a'}
    #         so given {'b','a'} is 'covered' for both 'c' & 'f' we know
    #            'a': {'d'}

    result = defaultdict(set)
    doubles = []
    singles = []
    for c, options in candidates.items():
        if len(options) == 1:
            if options not in singles:
                singles.append(options)
        if len(options) == 2:
            if options not in doubles:
                doubles.append(options)
    for c, options in candidates.items():
        if len(options) > 2:
            for sgl in singles:
                if sgl <= options:
                    options = options - sgl
            for dbl in doubles:
                if dbl <= options:
                    options = options - dbl
        result[c] = options
    return result


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
# print("test part 1:", part1(test_input))
# print("part 1:", part1(input))
print("test part 2:", part2(single_test_input))
#print("test part 2:", part2(test_input))
# print("part 2:", part2(input))
