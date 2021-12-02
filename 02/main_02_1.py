#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

depth = 0
horizontal_pos = 0

for line in input_:
    command, pos = line.split()
    pos = int(pos)
    if command == "forward":
        horizontal_pos += pos
    elif command == "up":
        depth -= pos
        depth = max(0, depth)
    elif command == "down":
        depth += pos

print(f"depth: {depth}")
print(f"horizontal pos: {horizontal_pos}")
print(f"product: {depth * horizontal_pos}")
