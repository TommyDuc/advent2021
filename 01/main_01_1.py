#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(this_dir + "/input", mode='r') as file:
    input_ = [int(line.strip()) for line in file.readlines() if line]

increase_count = 0
previous_depth = input_[0]
for depth in input_[1:]:
    if previous_depth < depth:
        increase_count += 1
    previous_depth = depth

print(increase_count)
