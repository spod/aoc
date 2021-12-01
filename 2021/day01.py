#! /usr/bin/env python

from itertools import combinations
test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input =  list((int(l.strip()) for l in open("./inputs/day01").readlines()))

def partA(input):
    prev_depth = -1
    depth_increases = 0
    for sweep in input:
        if sweep > prev_depth and prev_depth != -1:
            depth_increases += 1
        prev_depth = sweep
    return depth_increases

print("test partA:", partA(test_input))
print("partA:", partA(input))

def partB(input):
    # 3 measurement sliding window
    # [199, 200, 208, 210]
    # A, B = ((199, 200, 208), (200, 208, 210))
    # if sum(B) > sum(A) then depth_increase
    prev_sum = -1
    depth_increases = 0
    for i in range(len(input) - 3 + 1):
        # print(input[i: i + 3], sum(input[i: i + 3]))
        sweep_sum = sum(input[i: i + 3])
        if sweep_sum > prev_sum and prev_sum != -1:
            depth_increases += 1
        prev_sum = sweep_sum
    return depth_increases

print("test partB:", partB(test_input))
print("partB:", partB(input))
