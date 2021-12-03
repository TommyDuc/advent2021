#!/usr/bin/env python3

import os

this_dir = os.path.dirname(__file__)

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [int(line.strip()) for line in file.readlines() if line]

moving_sums = [sum(input_[i:i+3]) for i in range(len(input_)-2)]

answer = len(
    list(
        filter(
            lambda x: x[0] > x[1],
            list(
                zip(moving_sums[1:], moving_sums[:-1])
            )
        )
    )
)
print(answer)
