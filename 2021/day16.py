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

def parse_literal(bits):
    # literals are groups of 5 bits, first bit indicates if this is the last group or not
    remainder = bits
    literal = ''
    n = 0
    last = False
    while not last:
        last = bits[n] == '0'
        literal += bits[n+1:n+5]
        remainder = remainder[5:]
        n = n + 5
    return (int(literal, 2), remainder)


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
        last_rest = None
        rest = packet[20:]
        while len(rest) >= 5:
            (v, rest) = parse_literal(rest)
            print(v, ' ', rest, ' ', end = ' ')
        print()
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
        last_rest = None
        rest = packet[18:]
        # need to recursively call packet stuff ...
        while rest != last_rest and len(rest) >= 5:
            last_rest = rest
            (v, rest) = parse_literal(rest)
            print(v)


def part1(input):
    print()
    packet = hex2bin(input[0])
    versions = []
    versions.append(packet_version(packet))
    print(
        f"Debug info for packet: {input[0]} ({packet})\n - version: {packet_version(packet)}\n - type: {packet_type(packet)}")
    if packet_type(packet) == 4:
        print(f" - literal packet, value: {parse_literal_packet(packet)}")
    else:
        print(f" - operator packet, {parse_operator_packet(packet)}")
        # need to iterate through sub packets and get their versions added to version
    print()
    return sum(versions)


def part2(input):
    return None

print(parse_literal('01010000001100100000100011000001100000'))


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
for t in test_cases:
    print(f"test part1({t[0]}): {part1(t[0])}, should be: {t[1]}")
#print("part 1:", part1(input))
# for t in test_cases:
#     print(f"- test part2({t[0]}): {part2(t[0])}, should be: {t[1]}")
# print("part 2:", part2(input))
