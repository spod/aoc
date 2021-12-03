#! /usr/bin/env python

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]
input = list((l.strip() for l in open("./inputs/day03").readlines()))


def partA(input):
    # first count bits
    # for bit pos 0, count number of 1s in input in list 0
    obs_set_bit_count = []
    samples = len(input)
    sample_size = len(input[0])
    for _ in range(sample_size):
        obs_set_bit_count.append(0)

    for ob in input:
        i = 0
        for b in ob:
            if b == '1':
                obs_set_bit_count[i] += 1
            i += 1

    # now figure out gamma & epsilon binary
    gamma_s = ''
    epsilon_s = ''
    for ones in obs_set_bit_count:
        if ones > samples - ones:
            gamma_s += '1'
            epsilon_s += '0'
        else:
            gamma_s += '0'
            epsilon_s += '1'

    gamma = int(gamma_s, 2)
    epsilon = int(epsilon_s, 2)

    power = gamma * epsilon

    return power


# print("test partA:", partA(test_input))
# print("partA:", partA(input))


def input_to_matrix(input):
    result = []
    for sample in input:
        result.append([])
        for b in sample:
            result[-1].append(int(b))
    return result


def col(matrix, column):
    result = []
    for r in matrix:
        result.append(r[column])
    return result


def binlist2int(binlist):
    binstring = ''
    for b in binlist:
        binstring += str(b)
    return int(binstring, 2)


def filter_matrix(matrix, col, want):
    new_matrix = []
    for row in matrix:
        if row[col] == want:
            new_matrix.append(row)
    return new_matrix


def partB(input):
    dat = input_to_matrix(input)

    oxygen_dat = dat
    for b in range(len(dat[0])):
        c = col(oxygen_dat, b)
        if c.count(1) >= c.count(0):
            most_common = 1
        else:
            most_common = 0
        oxygen_dat = filter_matrix(oxygen_dat, b, most_common)
        if len(oxygen_dat) == 1:
            break
    oxygen = binlist2int(oxygen_dat[0])
    print(oxygen)

    co2_dat = dat
    for b in range(len(dat[0])):
        c = col(co2_dat, b)
        if c.count(1) < c.count(0):
            least_common = 1
        else:
            least_common = 0
        co2_dat = filter_matrix(co2_dat, b, least_common)
        if len(co2_dat) == 1:
            break
    co2 = binlist2int(co2_dat[0])

    return oxygen * co2


print("test partB:", partB(test_input))
print("partB:", partB(input))
