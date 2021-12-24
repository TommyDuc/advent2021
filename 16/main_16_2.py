#!/usr/bin/env python3
import os
from bitstring import BitStream
from functools import reduce

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.readline().strip()

data_ = BitStream(f"0x{input_}")


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

    def evaluate(self):
        raise NotImplementedError()


class Literal(Packet):
    def __init__(self, version, type_id, literal_value):
        super().__init__(version, type_id)
        self.value = literal_value

    def evaluate(self):
        return self.value


class Operator(Packet):
    op_dict = {
        0: lambda l, r: l+r,
        1: lambda l, r: l*r,
        2: lambda l, r: min(l, r),
        3: lambda l, r: max(l, r),
        5: lambda l, r: int(l > r),
        6: lambda l, r: int(l < r),
        7: lambda l, r: int(l == r)
    }

    def __init__(self, version, type_id, packets: list[Packet]):
        super().__init__(version, type_id)
        self.packets = packets

    def evaluate(self):
        return reduce(Operator.op_dict[self.type_id], map(lambda p: p.evaluate(), self.packets))


def read_packet(bitstream: BitStream) -> Packet:
    version = bitstream.read(fmt='bits:3').uint
    type_id = bitstream.read(fmt='bits:3').uint
    if type_id == 4:
        literal_value = read_literal(bitstream)
        return Literal(version, type_id, literal_value)
    else:
        operator_packets = read_operator(bitstream)
        return Operator(version, type_id, operator_packets)


def read_packets(bitstream: BitStream) -> list[Packet]:
    packets = list()
    while bitstream.pos != bitstream.len:
        packets.append(read_packet(bitstream))
    return packets


def read_literal(bitstream: BitStream):
    literal_bitstream = BitStream()
    while True:
        has_next = bitstream.read(fmt='bool')
        literal_bitstream.append(bitstream.read(fmt='bits:4'))
        if not has_next:
            break
    return literal_bitstream.uint


def read_operator(bitstream: BitStream) -> list[Packet]:
    length_type_id = bitstream.read(fmt='bits:1').uint
    operator_packets = list()
    if length_type_id == 0:
        sub_packets_length = bitstream.read(fmt='bits:15').uint
        packets_bitstream = bitstream.read(fmt=f'bits:{sub_packets_length}')
        bitstream_packets = read_packets(packets_bitstream)
        operator_packets.extend(bitstream_packets)
    else:
        sub_packets_count = bitstream.read(fmt='bits:11').uint
        for _ in range(sub_packets_count):
            operator_packets.append(read_packet(bitstream))
    return operator_packets


parent_packet = read_packet(data_)
answer = parent_packet.evaluate()
print(answer)
