#! /usr/bin/env python3
import os.path

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))

class Device:
    label: str
    outputs: list[str]

    def __init__(self, input_string: str):
        self.label = input_string[0:input_string.find(':')]
        self.outputs = input_string[input_string.find(':')+1:].split()

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Device(label: '{self.label}', outputs: {self.outputs})"


def part1(input: list[str]):
    devices: list[Device] = [Device(ln) for ln in input]
    print(devices)
    return None


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input: list[str]):
    return None


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
