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
        return f"Point({self.r}, {self.c})"

    def __repr__(self) -> str:
        return f"Point({self.r}, {self.c})"


def area(c1: Point, c2: Point) -> float:
    h = abs(c1.r - c2.r) + 1
    w = abs(c1.c - c2.c) + 1
    return h * w


def rectangle(c1: Point, c2: Point) -> tuple[Point, Point, Point, Point]:
    c3 = Point(c1.r, c2.c)
    c4 = Point(c2.r, c1.c)
    return (c1, c2, c3, c4)


class Line:
    p1: Point
    p2: Point

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"Line({self.p1}, {self.p2})"

    def __repr__(self) -> str:
        return f"Line({self.p1}, {self.p2})"

    def on_line(self, p3: Point) -> bool:
        return (self.p2.r - self.p1.r) * (p3.c - self.p1.c) == (p3.r - self.p1.r) * (
            self.p2.c - self.p1.c
        )

    def is_on(self, p3: Point) -> bool:
        result = False
        if self.p1.r != self.p2.r:
            result = self.on_line(p3) and within(self.p1.r, p3.r, self.p2.r)
        result = self.on_line(p3) and within(self.p1.c, p3.c, self.p2.c)
        # if result:
        #     print(f"{self}.is_on({p3}) - {result}")
        return result


def within(x: int, y: int, z: int) -> bool:
    # return true if y is between x and z
    return x <= y <= z or z <= y <= x


class Rectangle:
    c1: Point
    c2: Point

    def __init__(self, c1: Point, c2: Point):
        self.c1 = c1
        self.c2 = c2

    def __str__(self) -> str:
        return f"Rectangle({self.c1}, {self.c2})"

    def __repr__(self) -> str:
        return f"Rectangle({self.c1}, {self.c2})"

    def within(self, p3: Point) -> bool:
        result = within(self.c1.r, p3.r, self.c2.r) and within(
            self.c1.c, p3.c, self.c2.c
        )
        # if result:
        #     print(f"{self}.within({p3}) - {result}")
        return result


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
            if valid(n, self):
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


def sub_grid(g: Grid, tl: Point, br: Point) -> Grid:
    rg: list[list[str]] = []

    for r in range(tl.r, br.r + 1):
        rg.append([])
        for c in range(tl.c, br.c + 1):
            rg[r].append(g.get_value_at(Point(r, c)))

    return Grid(rg)
