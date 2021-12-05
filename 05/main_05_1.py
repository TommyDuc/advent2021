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

segments = list()
largest_coord = 0
for line in input_:
    groups = regex.match(line).groups()
    segment = Segment(*map(lambda x: int(x), groups))
    segments.append(segment)
    largest_coord = max(largest_coord, max(segment))
    pass
hv_lines = list(filter(lambda s: s.x1 == s.x2 or s.y1 == s.y2, segments))

map_ = dict()
for line in hv_lines:
    x_start = min(line.x1, line.x2)
    x_end = max(line.x1, line.x2)
    y_start = min(line.y1, line.y2)
    y_end = max(line.y1, line.y2)
    for x in range(x_start, x_end+1):
        for y in range(y_start, y_end+1):
            pos = (x, y)
            if pos not in map_:
                map_[pos] = 1
            else:
                map_[pos] += 1

answer = len(list(filter(lambda i: i >= 2, map_.values())))
print(answer)
