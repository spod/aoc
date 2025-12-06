class Point:
    r: int
    c: int

    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c

    # TODO research how to type magic methods like __add__
    def __add__(self, other):  # type: ignore
        return Point(self.r + other.r, self.c + other.c)  # type: ignore

    def __str__(self) -> str:
        return f"Cell({self.r}, {self.c})"

    def __repr__(self) -> str:
        return f"Cell({self.r}, {self.c})"


class Grid:
    rows: int
    cols: int
    g: list[list[str]]

    def __init__(self, g: list[list[str]]):
        self.g = g
        self.rows = len(self.g) - 1
        self.cols = len(self.g[0]) - 1

    def col_values(self, c: int) -> list[str]:
        result: list[str] = []
        for row in self.g:
            result.append(row[c])
        return result

    def row_values(self, r: int) -> list[str]:
        return self.g[r]

    def size(self) -> tuple[int, int]:
        return (self.rows, self.cols)

    def get_value_at(self, p: Point) -> str:
        return self.g[p.r][p.c]

    def set_value_at(self, p: Point, v: str):
        self.g[p.r][p.c] = v

    def adj_points(self, p: Point) -> list[Point]:
        offsets: list[Point] = [
            Point(-1, -1),
            Point(-1, 0),
            Point(-1, 1),
            Point(0, -1),
            Point(0, 1),
            Point(1, -1),
            Point(1, 0),
            Point(1, 1),
        ]
        results: list[Point] = []
        for o in offsets:
            n = p + o
            if n.valid(self):
                results.append(n)
        return results

    def adj_point_values(self, point: Point) -> list[str]:
        results: list[str] = []
        for p in self.adj_points(point):
            results.append(self.get_value_at(p))
        return results

    def print(self):
        for r in self.g:
            print(" ".join([str(c) for c in r]))


def valid(p: Point, g: Grid) -> bool:
    (max_r, max_c) = g.size()
    return p.r >= 0 and p.c >= 0 and p.r <= max_r and p.c <= max_c


def build_grid(input: list[str], fill: str = "") -> Grid:

    def char_or_fill(char: str, fill: str) -> str:
        if fill != "" and char == " ":
            return fill
        return char

    g: list[list[str]] = []
    for line in input:
        g.append([char_or_fill(c, fill) for c in line])
    return Grid(g)
