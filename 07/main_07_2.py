#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.read().split(',')

positions_list = list(map(lambda i: int(i), input_))
h_min, h_max = min(positions_list), max(positions_list)


def compute_cost(pos: int):
    costs = list(map(lambda i: abs(i - pos), positions_list))
    costs = list(map(lambda i: int((i*(i+1))/2), costs))
    return sum(costs)


lowest_cost = (h_min, compute_cost(h_min))
for candidate in range(h_min+1, h_max):
    cost = compute_cost(candidate)
    if cost < lowest_cost[1]:
        lowest_cost = (candidate, cost)

print(lowest_cost)
