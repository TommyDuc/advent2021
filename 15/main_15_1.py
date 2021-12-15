#!/usr/bin/env python3

import os
from itertools import product

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

grid = list()
for line in input_:
    grid.append(list(map(lambda c: int(c), line)))
height, width = len(grid), len(grid[0])
start, end = (0, 0), (height-1, width-1)
nodes_costs = dict()
for i, j in product(range(height), range(width)):
    nodes_costs[(i, j)] = None
nodes_costs[start] = 0


def neighbors_iter(i_, j_):
    global height
    global width
    if i_ > 0:
        yield i_-1, j_
    if i_ < height-1:
        yield i_+1, j_
    if j_ > 0:
        yield i_, j_-1
    if j_ < width-1:
        yield i_, j_+1


computed_nodes = set()
nodes_with_minimum_value = {start}
while len(computed_nodes) != height*width:
    tentative_nodes = list(sorted(iter(nodes_with_minimum_value - computed_nodes), key=lambda n: nodes_costs[n]))
    current_node = tentative_nodes[0]
    computed_nodes.add(current_node)

    for neighbor in neighbors_iter(*current_node):
        current_new_value = grid[neighbor[0]][neighbor[1]] + nodes_costs[current_node]
        if nodes_costs[neighbor] is None:
            nodes_costs[neighbor] = current_new_value
        else:
            nodes_costs[neighbor] = min(nodes_costs[neighbor], current_new_value)
        nodes_with_minimum_value.add(neighbor)

print(nodes_costs[end])

