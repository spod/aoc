#! /usr/bin/env python


import os.path
test_cases = [
    (["D2FE28"], None),
    (["38006F45291200"], None),
    (["EE00D40C823060"], 7),
    (["8A004A801A8002F478"], 16),
    # (["620080001611562C8802118E34"], 12),
    # (["C0015000016115A2E0802F182340"], 23),
    # (["A0016C880162017C3686B18A3D4780"], 31)
]


def hex2bin(line):
    return str(bin(int.from_bytes(bytes.fromhex(line), 'big')))[2:]


def packet_version(packet):
    # first 3 bits is packet version
    return int(packet[0:3], 2)


def packet_type(packet):
    # second 3 bits are packet type
    return int(packet[3:6], 2)


def parse_literal_packet(packet):
    if packet_type(packet) != 4:
        print("ERROR tried to parse operator packet as literal packet")
        return None
    return parse_literal(packet[6:])

def parse_literal(literal_bin):
    # literals are groups of 5 bits, first bit indicates if this is the last group or not
    print(f"parse_literal({literal_bin}) - ", end = ' ')
    literal = ''
    n = 0
    last = False
    while not last:
        last = literal_bin[n] == '0'
        print(f"n: {n}, raw: {literal_bin[n:n+5]}, last: {last}, rest: {literal_bin[n+1:n+5]}; ", end = ' ')
        literal += literal_bin[n+1:n+5]
        n = n + 5
    print(f' - literal: {literal}, {int(literal, 2)}')
    return int(literal, 2)


def parse_operator_packet(packet):
    if packet_type(packet) == 4:
        print("ERROR tried to parse literal packet as operator packet")
        return None
    length_type = packet[6]
    print(f"  - length type: {length_type}")
    # Operator Length Type 0
    #     00111000000000000110111101000101001010010001001000000000
    #     VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
    # idx 0123456789111111111122
    # idx           012345678901
    # 
    # val 1   0 0        27
    #
    if length_type == '0':
        print(f"  - 15 bit length ({packet[7:20]}) = {int(packet[7:20], 2)}")
        sub_packet_bits_to_read = int(packet[7:20], 2)
        print(f"    - TODO read {sub_packet_bits_to_read} bits of sub packets")
        print(f"      rest: {packet[20:]}")
    # Operator Length Type 1
    #     11101110000000001101010000001100100000100011000001100000
    #     VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
    # idx 0123456789111111111122
    # idx           012345678901
    # 
    # val 7   3 1      #
    if length_type == '1':
        print(f"  - 11 bit length ({packet[7:18]}) = {int(packet[7:18], 2)}")
        sub_packets_to_read = int(packet[7:18], 2)
        print(f"    - TODO read {sub_packets_to_read} sub packets")
        print(f"      rest: {packet[18:]}")


print(parse_literal('101111111000101000')) # 2021
# 11010001010
# 11010
# 1 more, 1010 (10)
# 00101
# 0 last, 0101 (5)
# print(parse_literal('11010001010')) #10
# print(parse_literal('1101000101001010010001001000000000'))
# print(parse_literal('01010010001001000000000'))
# print(parse_literal('0101001000100100'))
# print(parse_literal('01010000001'))
# print(parse_literal('10010000010'))
# print(parse_literal('0011000001100000'))
#import sys; sys.exit(0)

def part1(input):
    print()
    packet = hex2bin(input[0])
    print(
        f"Debug info for packet: {input[0]} ({packet})\n - version: {packet_version(packet)}\n - type: {packet_type(packet)}")
    if packet_type(packet) == 4:
        print(f" - literal packet, value: {parse_literal_packet(packet)}")
    else:
        print(f" - operator packet, {parse_operator_packet(packet)}")
    print()
    return None


def part2(input):
    return None


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
for t in test_cases:
    print(f"test part1({t[0]}): {part1(t[0])}, should be: {t[1]}")
#print("part 1:", part1(input))
# for t in test_cases:
#     print(f"- test part2({t[0]}): {part2(t[0])}, should be: {t[1]}")
# print("part 2:", part2(input))
