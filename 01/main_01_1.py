#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [int(line.strip()) for line in file.readlines() if line]

answer = len(
    list(
        filter(
            lambda x: x[0] > x[1],
            list(
                zip(input_[1:], input_[:-1])
            )
        )
    )
)
print(answer)
