#!/usr/bin/env python3

from itertools import product
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

grid = list()
for line in input_:
    numbers = [int(i) for i in line if i != '\n']
    grid.append(numbers)
height, width = len(grid), len(grid[0])


def get_grid_factor(i_, j_):
    current = grid[i_][j_]
    neighbors_ = list()

    if i_ != 0:
        neighbors_.append(grid[i_ - 1][j_])
    if i_ != height-1:
        neighbors_.append(grid[i_ + 1][j_])
    if j_ != 0:
        neighbors_.append(grid[i_][j_ - 1])
    if j_ != width-1:
        neighbors_.append(grid[i_][j_ + 1])

    for neighbor_ in neighbors_:
        if current >= neighbor_:
            return 0

    return current + 1


answer = 0
for i, j in product(range(height), range(width)):
    answer += get_grid_factor(i, j)

print(answer)
