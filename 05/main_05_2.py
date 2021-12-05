#!/usr/bin/env python3

from collections import namedtuple
import re
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

input__ = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"]

regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
Segment = namedtuple("Segment", "x1 y1 x2 y2")


def get_range(n1, n2):
    if n1 == n2:
        return [n1]
    elif n1 < n2:
        return list(range(n1, n2+1))
    else:
        return list(range(n1, n2-1, -1))


def add_to_map(x_, y_):
    pos_ = (x_, y_)
    if pos_ in map_:
        map_[pos_] += 1
    else:
        map_[pos_] = 1


segments = list()
for line in input_:
    groups = regex.match(line).groups()
    segment = Segment(*map(lambda x: int(x), groups))
    segments.append(segment)
    pass

map_ = dict()
hv_lines = list(filter(lambda s: s.x1 == s.x2 or s.y1 == s.y2, segments))
diagonal_lines = list(filter(lambda s: not (s.x1 == s.x2 or s.y1 == s.y2), segments))

for line in hv_lines:
    if line.x1 == line.x2:
        y_range = get_range(line.y1, line.y2)
        for y in y_range:
            add_to_map(line.x1, y)
    elif line.y1 == line.y2:
        x_range = get_range(line.x1, line.x2)
        for x in x_range:
            add_to_map(x, line.y1)
    else:
        raise Exception()

for line in diagonal_lines:
    coordinates = zip(get_range(line.x1, line.x2), get_range(line.y1, line.y2))
    for coordinate in coordinates:
        add_to_map(*coordinate)

answer = len(list(filter(lambda i: i >= 2, map_.values())))
print(answer)
