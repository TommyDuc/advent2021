#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

aim = 0
depth = 0
horizontal_pos = 0

for line in input_:
    command, pos = line.split()
    pos = int(pos)
    if command == "forward":
        horizontal_pos += pos
        depth += aim * pos
    elif command == "up":
        aim -= pos
        aim = max(0, aim)
    elif command == "down":
        aim += pos

print(f"depth: {depth}")
print(f"horizontal pos: {horizontal_pos}")
print(f"product: {depth * horizontal_pos}")
