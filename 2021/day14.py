#! /usr/bin/env python

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
    steps = 1
    while steps < 10 + 1:
        template = step(template, rules)
        steps += 1
    
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


def part2(input):
    return None


import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
# print("test part 2:", part2(test_input))
# print("part 2:", part2(input))