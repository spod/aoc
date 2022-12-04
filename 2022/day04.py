#! /usr/bin/env python
import os.path
day = os.path.basename(__file__).split('.')[0][-2:]
print(f"Day {day}")

test_input_raw = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

def parse_line(line):
    l,r = line.split(",")
    lmin,lmax = l.split("-")
    lmin, lmax = int(lmin), int(lmax)
    rmin,rmax = r.split("-")
    rmin, rmax = int(rmin), int(rmax)
    return ((lmin, lmax), (rmin, rmax))

def part1(input):
    count = 0
    for line in input:
        if line != "":
            lrange, rrange = parse_line(line)
            lset = set(range(lrange[0], lrange[1]+1))
            rset = set(range(rrange[0], rrange[1]+1))
            if lset.issubset(rset) or rset.issubset(lset):
                # print(line)
                count+=1
    return count

print("test part 1:", part1(test_input))
print("part 1:", part1(input))

def part2(input):
    count = 0
    for line in input:
        if line != "":
            lrange, rrange = parse_line(line)
            lset = set(range(lrange[0], lrange[1]+1))
            rset = set(range(rrange[0], rrange[1]+1))
            if lset & rset:
                # print(line)
                count+=1
    return count
print("test part 2:", part2(test_input))
print("part 2:", part2(input))