#! /usr/bin/env python3
import os.path


day = os.path.basename(__file__).split(".")[0][-2:]
print(f"Day {day}")

test_input_raw = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

# TODO - move Grid and Cell into a helper library? Maybe tomorrow
type Grid = list[list[str]]


class Cell:
    r: int
    c: int

    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c

    # TODO research how to type magic methods like __add__
    def __add__(self, other):  # type: ignore
        return Cell(self.r + other.r, self.c + other.c)  # type: ignore

    def __str__(self) -> str:
        return f"Cell({self.r}, {self.c})"

    def __repr__(self) -> str:
        return f"Cell({self.r}, {self.c})"

    def valid(self, g: Grid) -> bool:
        (max_r, max_c) = g_size(g)
        return self.r >= 0 and self.c >= 0 and self.r <= max_r and self.c <= max_c


# TODO make a typed Grid class
def g_size(g: Grid) -> tuple[int, int]:
    #     max_r = len(grid) - 1
    # max_c = len(grid[0]) - 1
    return (len(g) - 1, len(g[0]) - 1)


def g_cell_value(g: Grid, c: Cell) -> str:
    return g[c.r][c.c]


def g_set_cell_value(g: Grid, c: Cell, v: str):
    g[c.r][c.c] = v


def build_grid(input: list[str]) -> Grid:
    g: Grid = []
    for line in input:
        g.append([c for c in line])
    return g


def g_adj_cells(grid: Grid, c: Cell) -> list[Cell]:
    offsets: list[Cell] = [
        Cell(-1, -1),
        Cell(-1, 0),
        Cell(-1, 1),
        Cell(0, -1),
        Cell(0, 1),
        Cell(1, -1),
        Cell(1, 0),
        Cell(1, 1),
    ]
    results: list[Cell] = []
    for o in offsets:
        n = c + o
        if n.valid(grid):
            results.append(n)
    return results


def g_adj_cell_values(grid: Grid, cell: Cell) -> list[str]:
    results: list[str] = []
    for c in g_adj_cells(grid, cell):
        results.append(g_cell_value(grid, c))
    return results


def g_print(g: Grid):
    for r in g:
        print(" ".join([str(c) for c in r]))


test_input = list(ln.strip() for ln in test_input_raw.splitlines())
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


def part1(input: list[str]):
    grid = build_grid(input)
    (max_r, max_c) = g_size(grid)
    accessible_rolls: list[Cell] = []
    for r in range(0, max_r + 1):
        for c in range(0, max_c + 1):
            cc = Cell(r, c)
            # this line took so long to figure out, read spec carefully
            if g_cell_value(grid, cc) == "@":
                neighbours = g_adj_cell_values(grid, cc)
                if neighbours.count("@") < 4:
                    accessible_rolls.append(cc)
    return len(accessible_rolls)


print("test part 1:", part1(test_input))
print("part 1:", part1(input))


def part2(input: list[str]):
    grid = build_grid(input)
    (max_r, max_c) = g_size(grid)

    removed_rolls: list[Cell] = []
    removed_last = 1

    while removed_last != 0:
        accessible_rolls: list[Cell] = []
        for r in range(0, max_r + 1):
            for c in range(0, max_c + 1):
                cc = Cell(r, c)
                if g_cell_value(grid, cc) == "@":
                    neighbours = g_adj_cell_values(grid, cc)
                    if neighbours.count("@") < 4:
                        g_set_cell_value(grid, cc, ".")
                        accessible_rolls.append(cc)
        removed_rolls.extend(accessible_rolls)
        removed_last = len(accessible_rolls)
    return len(removed_rolls)


print("test part 2:", part2(test_input))
print("part 2:", part2(input))
