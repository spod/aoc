from typing import Self


class Range:
    min: int
    max: int

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def __lt__(self, other: Self) -> bool:
        return (self.min, self.max) < (other.min, other.max)

    def __repr__(self) -> str:
        return f"Range({self.min},{self.max})"

    def __str__(self) -> str:
        return f"Range({self.min},{self.max})"

    def contains(self, value: int) -> bool:
        return value >= self.min and value <= self.max

    def size(self) -> int:
        return self.max + 1 - self.min


def merge_ranges(input: list[Range]) -> list[Range]:
    merged: list[Range] = []
    input.sort()
    merged = [input[0]]
    for rng in input[1:]:
        if merged[-1].max >= rng.min:
            merged[-1] = Range(merged[-1].min, max(merged[-1].max, rng.max))
        else:
            merged.append(rng)
    return merged
