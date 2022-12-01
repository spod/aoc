#! /usr/bin/env python

test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

input = open("./inputs/day01").read()


def partA(input):
    currTotal = 0
    maxTotal = 0
    for line in input.split("\n"):
        if line == "":
            if currTotal > maxTotal:
                maxTotal = currTotal
            currTotal = 0
            continue
        currTotal += int(line)
    return maxTotal


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
    totals = []
    currTotal = 0
    for line in input.split("\n"):
        if line == "":
            totals.append(currTotal)
            currTotal = 0
            continue
        currTotal += int(line)
    totals.append(currTotal)
    totals = sorted(totals, reverse=True)
    return sum(totals[:3])


print("test partB:", partB(test_input))
print("partB:", partB(input))
