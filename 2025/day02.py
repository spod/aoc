#! /usr/bin/env python3
import os.path

day = os.path.basename(__file__).split(".")[0][-2:]

test_input_raw = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""
test_input = list(ln.strip() for ln in test_input_raw.splitlines())
test_input.remove("")
input = list((ln.strip() for ln in open(f"./inputs/day{day}").readlines()))


def silly_ids(idRange: str) -> list[int]:
    silly: list[int] = []
    left, right = idRange.split("-")
    minId = int(left)
    maxId = int(right)
    for v in range(minId, maxId + 1):
        sv = str(v)
        if len(sv) % 2 == 0:
            m = int(len(sv) / 2)
            left = sv[:m]
            right = sv[m:]
            if left == right:
                # print(f"invalid ID: {sv}")
                silly.append(v)
    return silly


def partA(input: list[str]):
    sillyIds: list[int] = []
    idRanges = input[0].split(",")
    for idRange in idRanges:
        sillyIds.extend(silly_ids(idRange))
    # print(sillyIds)
    return sum(sillyIds)


print("test partA:", partA(test_input))
print("partA:", partA(input))


def invalid(id: str):
    # 12341234 - 1234, 1234 above
    # 123123123 - 123, 123, 123 - 123 x 3
    # 1212121212 - 12, 12, 12, 12, 12 - 12 x 5
    # 1111111 - 1, 1, 1, 1, 1, 1, 1 - 1 x 7
    midp = int(len(id) / 2)
    length = len(id)
    for k in range(1, midp + 1):
        repeats, remainder = divmod(length, k)
        if remainder == 0:
            candidate = id[:k] * repeats
            if id == candidate:
                return True
    return False


def check_range(idRange: str) -> list[int]:
    silly: list[int] = []
    left, right = idRange.split("-")
    minId = int(left)
    maxId = int(right)
    for v in range(minId, maxId + 1):
        if invalid(str(v)):
            silly.append(v)
    return silly


def partB(input: list[str]):
    sillyIds: list[int] = []
    idRanges = input[0].split(",")
    for idRange in idRanges:
        sillyIds.extend(check_range(idRange))
    # print(sillyIds)
    return sum(sillyIds)


# test_values = ["1", "12", "12341234", "1212121212", "1111111"]
# for tc in test_values:
#     print(f"{tc}: {invalid(tc)}")

print("test partB:", partB(test_input))
print("partB:", partB(input))
