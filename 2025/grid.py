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
