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
    ls_output = False
    for line in input[1:]:
        if line[0] == "$":
            ls_output = False
            command = line.split()[1]
            if command == "cd":
                cd_arg = line.split()[2]
                if cd_arg == "..":
                    pwd = os.path.dirname(pwd)
                else:
                    pwd = os.path.join(pwd, cd_arg)
            if command == "ls":
                ls_output = True
                continue
        elif ls_output:
            (a, _) = line.split()
            if a == "dir":
                continue
            else:
                fsize = int(a)
                dir_sizes[pwd] += fsize
                d = pwd
                while os.path.dirname(d) != d:
                    d = os.path.dirname(d)
                    dir_sizes[d] += fsize
    return dir_sizes


def part1(input):
    dir_sizes = get_dir_sizes(input)
    total_lte_10k = 0
    for dsize in dir_sizes.values():
        if dsize <= 100000:
            total_lte_10k += dsize

    return total_lte_10k


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    dir_sizes = get_dir_sizes(input)

    disk_size = 70000000
    update_size = 30000000
    used_size = dir_sizes["/"]
    unused_size = disk_size - used_size
    if unused_size < update_size:
        space_needed = update_size - unused_size

    deletion_candidates = []
    for d, dsize in dir_sizes.items():
        if dsize >= space_needed:
            deletion_candidates.append((d, dsize))

    candidate_sizes = [dt[1] for dt in deletion_candidates]
    candidate_sizes.sort()
    return candidate_sizes[0]


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
