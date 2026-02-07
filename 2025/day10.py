#! /usr/bin/env python3
import os.path

day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


class Lights:
    state: list[bool]
    goal: list[bool]

    def __init__(self, lights_input: str):
        # '[.##.]' 
        self.state = [False for _ in range(0, len(lights_input.strip()) - 2)]
        self.goal = [self._sym_to_bool(ch) for ch in lights_input[1:-1]]

    def __str__(self):
        return f"Lights(state: '{self._list_to_str(self.state)}', goal: '{self._list_to_str(self.goal)}')"

    def __repr__(self):
        return str(self)
    def _sym_to_bool(self, sym: str) -> bool:
        if sym == "#":
            return True
        elif sym == ".":
            return False
        else:
            print(f"invalid input: {sym}")
            return False

    def _bool_to_sym(self, bl: bool) -> str:
        if bl:
            return "#"
        return "."

    def _list_to_str(self, state: list[bool]) -> str:
        result: list[str] = ["["]
        for sym in state:
            result.append(self._bool_to_sym(sym))
        result.append("]")
        return "".join(result)


class Buttons:
    schematics: list[list[int]]

    def __init__(self, buttons_input: str):
        # (3) (1,3) (2) (2,3) (0,2) (0,1) -> [[3], [1,3], [2], [2,3], [0,2], [0,1]]
        result: list[list[int]] = []
        for char in buttons_input:
            match char:
                case '(':
                    result.append([])
                case ')':
                    continue
                case ',':
                    continue
                case ' ':
                    continue
                case _:
                    result[-1].append(int(char))
        self.schematics = result

    def __str__(self):
        return f"Buttons(schematics: '{self.schematics}')"
        
    def __repr__(self):
        return str(self)   


def parse_input(input: list[str]) -> tuple[list[Lights], list[Buttons]]:
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    lights: list[Lights] = []
    buttons: list[Buttons] = []
    for line in input:
        lights.append(Lights(line[0:line.find(']')]))
        buttons.append(Buttons(line[line.find(']') + 1: line.find('{') - 1].strip()))
    return (lights, buttons)


def part1(input: list[str]):
    (lights, buttons) = parse_input(input)
    for k in range(len(lights)):
        print(f"p{k}: {lights[k]}, {buttons[k]}")
    return None


print("test part 1:", part1(test_input))
import sys; sys.exit()
print("part 1:", part1(input))


def part2(input: list[str]):
    return None


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
