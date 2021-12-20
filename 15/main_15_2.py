#!/usr/bin/env python3

import os
from itertools import product

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

template_grid = list()
for line in input_:
    template_grid.append(list(map(lambda c: int(c), line)))
template_height, template_width = len(template_grid), len(template_grid[0])
height, width = 5*template_height, 5*template_width

grid = list()
for i in range(height):
    row = list()
    for j in range(width):
        i_template = i % template_height
        j_template = j % template_width
        offset_i, offset_j = int(i/template_height), int(j/template_width)
        new_value = template_grid[i_template][j_template] + offset_i + offset_j
        while new_value > 9:
            new_value -= 9
        row.append(new_value)
    grid.append(row)

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
    if len(computed_nodes) % 1000 == 0:
        print(height*width - len(computed_nodes))
    current_node = min(iter(nodes_with_minimum_value - computed_nodes), key=lambda n: nodes_costs[n])
    computed_nodes.add(current_node)

    for neighbor in neighbors_iter(*current_node):
        current_new_value = grid[neighbor[0]][neighbor[1]] + nodes_costs[current_node]
        if nodes_costs[neighbor] is None:
            nodes_costs[neighbor] = current_new_value
        else:
            nodes_costs[neighbor] = min(nodes_costs[neighbor], current_new_value)
        nodes_with_minimum_value.add(neighbor)

print(nodes_costs[end])

