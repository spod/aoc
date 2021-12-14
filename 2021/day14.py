#! /usr/bin/env python

import os.path
from collections import namedtuple, defaultdict

test_input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]

# so science, ahem
elements = [chr(x) for x in range(ord('A'), ord('Z') + 1)]


def read_input(input):
    template = input[0]
    rules = {}
    for line in input[1:]:
        if line != "":
            (pair, inserts) = line.split(' -> ')
            rules[pair] = inserts
    return (template, rules)


def step(template, rules):
    newtemplate = ""
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if newtemplate == "":
            newtemplate += pair[0]
        newtemplate += rules[pair] + pair[1]
    return newtemplate


def part1(input):
    template, rules = read_input(input)
    s = 0
    steps = 10
    while s < steps + 1:
        template = step(template, rules)
        s += 1

    min_e = 100000
    max_e = -1
    element_counts = {}
    for e in elements:
        element_counts[e] = template.count(e)
        if element_counts[e] < min_e and element_counts[e] != 0:
            min_e = element_counts[e]
        if element_counts[e] > max_e:
            max_e = element_counts[e]
    # print(min_e, max_e, element_counts)
    return max_e - min_e


# We can't just keep growing a string exponentially!
# Instead we store inner polymer as counts of pairs

Pair = namedtuple('Pair', ['left', 'right'])


class Polymer:
    def __init__(self, polymer, rules):
        self.rules = {}
        for r, i in rules.items():
            self.rules[Pair(r[0], r[1])] = i
        self.edge = Pair(polymer[0], polymer[-1])
        self.inner = defaultdict(int)
        for i in range(0, len(polymer) - 1):
            pair = Pair(polymer[i], polymer[i+1])
            self.inner[pair] += 1
        # print(f"Polymer<edge={self.edge}, inner={self.inner}>")

    def grow(self):
        pairs = defaultdict(int)
        for pair, count in self.inner.items():
            insert = self.rules[pair]
            pairs[Pair(pair.left, insert)] += count
            pairs[Pair(insert, pair.right)] += count
        self.inner = pairs

    def frequencies(self):
        freq = defaultdict(int)

        freq[self.edge.left] += 1
        freq[self.edge.right] += 1

        for pair, count in self.inner.items():
            freq[pair.left] += count
            freq[pair.right] += count
        min_e = 0
        max_e = 0
        for v in freq.values():
            if min_e == 0 and max_e == 0 and v != 0:
                min_e = v
                max_e = v
            elif v < min_e and v != 0:
                min_e = v
            elif v > max_e:
                max_e = v
        return int((max_e - min_e)/2)


def part2(input):
    template, rules = read_input(input)
    s = 0
    # print(template)
    p = Polymer(template, rules)
    steps = 39
    while s < steps + 1:
        p.grow()
        s += 1
    return p.frequencies()


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
# print("should be: 2188189693529")
print("part 2:", part2(input))
