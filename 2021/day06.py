#! /usr/bin/env python

test_input = [
    "3,4,3,1,2"
]

def simulate(sea, days):
    day = 0
    
    while day < days:
        day += 1
        for fish in range(len(sea)):
            if sea[fish] == 0:
                sea[fish] = 6
                sea.append(8)
            else:
                sea[fish] -= 1
        # print(day, len(sea), sea)

    return len(sea)

def part1(input):
    sea = [int(x) for x in input[0].split(',')]
    return simulate(sea, 80)



def part2(input):
    sea = [int(x) for x in input[0].split(',')]
    return simulate(sea, 256)


import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
print("part 1:", part1(input))
print("test part 2:", part2(test_input))
# print("part 2:", part2(input))