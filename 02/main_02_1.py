#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip().split() for line in file.readlines() if line]

depth = 0
position_x = 0


def forward(x):
    global position_x
    position_x += x


def up(x):
    global depth
    depth -= x
    depth = max(0, depth)


def down(x):
    global depth
    depth += x


actions = {
    "forward": forward,
    "up": up,
    "down": down
}


for command_val in input_:
    actions[command_val[0]](int(command_val[1]))

print(depth * position_x)
