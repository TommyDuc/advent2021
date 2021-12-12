#!/usr/bin/env python3

from itertools import product
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

grid = list()
for line in input_:
    grid.append(list(map(lambda n: int(n), line)))


def grid_iter():
    return product(range(10), range(10))


def neighbors_iter(i_, j_):
    for i2, j2 in product([i_-1, i_, i_+1], [j_-1, j_, j_+1]):
        if (i2, j2) != (i_, j_) and 0 <= i2 <= 9 and 0 <= j2 <= 9:
            yield i2, j2


def do_cycle():
    flash_counter = 0

    for i_, j_ in grid_iter():
        grid[i_][j_] += 1

    has_changed = True
    while has_changed:
        has_changed = False
        for i_, j_ in grid_iter():
            if grid[i_][j_] > 9:
                grid[i_][j_] = 0
                flash_counter += 1
                has_changed = True
                for i2, j2 in neighbors_iter(i_, j_):
                    if grid[i2][j2] > 0:
                        grid[i2][j2] += 1
    return flash_counter


cycle = 0
while True:
    cycle += 1
    flash_count = do_cycle()
    if flash_count == 100:
        print(cycle)
        break
