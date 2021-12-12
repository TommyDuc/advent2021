#!/usr/bin/env python3

from itertools import product
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

raw_grid = list()
for line in input_:
    raw_grid.append(list(map(lambda n: int(n), line)))


def grid_iter():
    return product(range(10), range(10))


def neighbors_iter(i_, j_):
    for i2, j2 in product([i_-1, i_, i_+1], [j_-1, j_, j_+1]):
        if (i2, j2) != (i_, j_) and 0 <= i2 <= 9 and 0 <= j2 <= 9:
            yield i2, j2


flash_counter = 0


def do_cycle2():
    for i_, j_ in grid_iter():
        raw_grid[i_][j_] += 1

    has_changed = True
    while has_changed:
        has_changed = False
        global flash_counter
        for i_, j_ in grid_iter():
            if raw_grid[i_][j_] > 9:
                raw_grid[i_][j_] = 0
                flash_counter += 1
                has_changed = True
                for i2, j2 in neighbors_iter(i_, j_):
                    if raw_grid[i2][j2] > 0:
                        raw_grid[i2][j2] += 1


for cycle in range(1, 101):
    do_cycle2()

print(flash_counter)
