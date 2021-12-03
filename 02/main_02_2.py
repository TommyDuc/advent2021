#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip().split() for line in file.readlines() if line]

aim = 0
depth = 0
position_x = 0


def forward(x):
    global aim
    global depth
    global position_x
    position_x += x
    depth += aim * x


def up(x):
    global aim
    aim -= x


def down(x):
    global aim
    aim += x


actions = {
    "forward": forward,
    "up": up,
    "down": down
}

for command_val in input_:
    actions[command_val[0]](int(command_val[1]))

print(position_x * depth)
