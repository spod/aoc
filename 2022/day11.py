#! /usr/bin/env python
import os.path
import sys
from dataclasses import dataclass
import math

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


@dataclass
class Monkey:
    id: int
    items: list
    operation: None
    denominator: None
    targets: dict
    inspected: int

    def __init__(self):
        self.id = None
        self.items = []
        self.operation = None
        self.denominator = None
        self.targets = {True: None, False: None}
        self.inspected = 0

    def catch(self, item):
        self.items.append(item)


test_input = list(l.strip() for l in test_input_raw.splitlines())
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))


def load_monkeys(input):
    monkeys = {}

    currMonkey = None
    for line in input:
        # "Monkey 2:"
        if line.find("Monkey") >= 0:
            m = Monkey()
            sId = line.split()[1][:-1]
            m.id = int(sId)
            monkeys[m.id] = m
            currMonkey = m.id
            continue

        # "  Starting items: 74"
        if line.find("Starting items") >= 0:
            m = monkeys[currMonkey]
            sItems = line.split(":")[1]
            sItems = sItems.split(",")
            m.items = [int(i) for i in sItems]
            continue

        # "  Operation: new = old + 3"
        if line.find("Operation:") >= 0:
            m = monkeys[currMonkey]
            sExpr = line.split("=")[1]
            m.operation = eval(f"lambda old: {sExpr.strip()}")
            continue

        # "  Test: divisible by 3"
        if line.find("Test: divisible by") >= 0:
            m = monkeys[currMonkey]
            m.denominator = int(line.split()[3])
            continue

        # "If true: throw to monkey 2"
        if line.find("If true:") >= 0:
            m = monkeys[currMonkey]
            target = int(line.split()[-1])
            m.targets[True] = target
            continue

        # " If false: throw to monkey 3"
        if line.find("If false:") >= 0:
            m = monkeys[currMonkey]
            target = int(line.split()[-1])
            m.targets[False] = target
            continue

    return monkeys


def vprint(verbose, msg):
    if verbose:
        print(msg)


def play_round(monkeys, verbose, lcm=0):
    vprint(verbose, "Starting round")
    for m in sorted(monkeys.keys()):
        monkey = monkeys[m]
        # vprint(verbose, f"Monkey {monkey.id}:")

        to_remove = []

        for item in monkey.items:
            # vprint(verbose, f"Monkey inspects an item with a worry level of {item}.")
            worry = monkey.operation(item)
            # vprint(verbose, f"Worry level is ... to {worry}.")
            if lcm != 0:
                worry = monkey.operation(item) % lcm
            else:
                worry = monkey.operation(item) // 3

            # vprint(verbose, f"Monkey gets bored with item. Worry level is divided by 3 to {worry}.")
            divisible = worry % monkey.denominator == 0
            # if divisible:
            #     vprint(verbose, f"Current worry level is divisible by {monkey.denominator}.")
            # else:
            #     vprint(verbose, f"Current worry level is not divisible by {monkey.denominator}.")
            # vprint(verbose, f"Item with worry level {worry} is thrown to monkey {monkey.targets[divisible]}.")
            monkeys[monkey.targets[divisible]].catch(worry)
            monkey.inspected += 1
            to_remove.append(item)
        # can't mutate list as we iterate so remove only after we are done iterating through items
        for rm in to_remove:
            monkey.items.remove(rm)
    # vprint(verbose, "Finished round")


def monkey_status(monkeys):
    for _, m in monkeys.items():
        print(f"Monkey {m.id}: inspected: {m.inspected} items; items: {m.items}")


def part1(input):
    monkeys = load_monkeys(input)

    for round in range(1, 20 + 1):
        play_round(monkeys, False, 0)
        # play_round(monkeys, True)
        # print(f"status after round: {round}")
        # monkey_status(monkeys)

    inspections = [m.inspected for m in monkeys.values()]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input):
    monkeys = load_monkeys(input)

    # items get waaay too big so calculate least common multiple of all denominators
    # to use as a shortcut for divisble tests when each monkey is checking items
    lcm = math.lcm(*[m.denominator for m in monkeys.values()])

    for round in range(1, 10_000 + 1):
        play_round(monkeys, False, lcm)
        # play_round(monkeys, True)

    print(f"status after round: {round}")
    monkey_status(monkeys)

    inspections = [m.inspected for m in monkeys.values()]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
