#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.read().split(',')

fishes = list(map(lambda f: int(f), input_))

for gen in range(80):
    for i_fish in range(len(fishes)):
        fish = fishes[i_fish]
        if fish == 0:
            fishes.append(8)
            fishes[i_fish] = 6
        else:
            fishes[i_fish] -= 1

answer = len(fishes)
print(answer)
