#! /usr/bin/env python
import os.path
from dataclasses import dataclass

day = os.path.basename(__file__).split('.')[0][-2:]
print(f"Day {day}")

test_input_raw = """
noop
addx 3
addx -5
"""

test2_input_raw = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

test_input = list(l.strip() for l in test_input_raw.splitlines())
test2_input = list(l.strip() for l in test2_input_raw.splitlines())

input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))

@dataclass
class SimpleCpu:
    X: int
    
    def __init__(self):
        self.X = 1
        self.instructions = []
        self.pc = 0
        self.loading = False
        self.executing = None
        self.halted = False

    def tick(self):
        #print(f"tick start- pc: {self.pc}, X: {self.X}, loading: {self.loading}, executing: {self.executing}, halted: {self.halted}")
        
        if self.halted:
            return
    
        if not self.loading:
        
            self.executing = self.instructions[self.pc]

            match self.executing[0]:
                case "noop":
                    self.loading = False
                
                case "addx":
                    self.loading = True
                    self.pc -= 1 # stall

        else:
            # loading addx post stall
            self.X += self.executing[1]
            self.loading = False
            self.executing = False

        self.pc += 1

        if self.pc >= len(self.instructions):
            self.halted = True
    
        #print(f"tick end- pc: {self.pc}, X: {self.X}, loading: {self.loading}, executing: {self.executing}, halted: {self.halted}")


    def load(self, instructions):
        for l in instructions:
            if l == "noop":
                self.instructions.append((l, None))
            else:
                (instr, param) = l.split()
                param = int(param)
                self.instructions.append((instr, param))

def part1(input):
    if "" in input:
        input.remove("")

    cpu = SimpleCpu()
    cpu.load(input)
    strengths = []
    cycle = 0
    while cycle < 220 + 1:
        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths.append(cpu.X * cycle)
            print(f"cycle: {cycle}, X: {cpu.X}, strength: {cpu.X * cycle}, strengths: {strengths}")
        cpu.tick()
        cycle += 1
    
    return sum(strengths)

print("test part 1:", part1(test_input))
print()
print("test part 1, test 2:", part1(test2_input))
print()
print("part 1:", part1(input))

def part2(input):
    if "" in input:
        input.remove("")
    
    
    return None

print("test part 2:", part2(test_input))
print("part 2:", part2(input))