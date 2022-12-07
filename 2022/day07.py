#! /usr/bin/env python
import os.path
from collections import defaultdict

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

if "" in test_input:
    test_input.remove("")


def get_dir_sizes(input):
    dir_sizes = defaultdict(int)
    pwd = "/"
    for line in input[1:]:
        if line[0] == "$":
            if line[2:4] == "ls":
                continue  # skip to next line as we assume non command output is ls output
            (cmd, arg) = line[1:].split()
            if cmd == "cd":
                if arg == "..":
                    pwd = os.path.dirname(pwd)
                else:
                    pwd = os.path.join(pwd, arg)
        else:
            if line[0:3] == "dir":
                continue
            fsize = int(line.split()[0])
            dir_sizes[pwd] += fsize
            # also need to increase size of all parent directories
            d = pwd
            while os.path.dirname(d) != d:
                d = os.path.dirname(d)
                dir_sizes[d] += fsize
    return dir_sizes


def part1(input):
    dir_sizes = get_dir_sizes(input)
    return sum(filter(lambda sz: sz <= 100000, dir_sizes.values()))


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    dir_sizes = get_dir_sizes(input)
    space_needed = 30000000 - (70000000 - dir_sizes["/"])
    deletion_candidates = list(
        filter(lambda sz: sz >= space_needed, dir_sizes.values())
    )
    deletion_candidates.sort()
    return deletion_candidates[0]


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
