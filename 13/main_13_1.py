#!/usr/bin/env python3

import os
from itertools import product

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.read()
points_lines, folds_lines = input_.split('\n\n')

points = set()
width, height = 0, 0
for point_line in points_lines.split():
    x_str, y_str = point_line.split(',')
    point = (int(x_str), int(y_str))
    width, height = max(width, point[0]+1), max(height, point[1]+1)
    points.add(point)

folds = list()
for fold_line in folds_lines.split('\n'):
    if not fold_line:
        continue
    _0, _1, fold_str = fold_line.split()
    axis, coord = fold_str.split('=')
    folds.append((axis, int(coord)))


def print_points():
    for y_ in range(height):
        line = ""
        for x_ in range(width):
            line += '#' if (x_, y_) in points else '.'
        print(line)


def fold_along_x(axis_coord_: int):
    global width
    for coord_ in filter(lambda p: p[0] == axis_coord_, points):
        points.remove(coord_)

    for x_, y_ in product(range(axis_coord_), range(height)):
        other_point = (width-x_-1, y_)
        if other_point not in points:
            continue
        points.add((x_, y_))
        points.remove(other_point)
    width = axis_coord_


def fold_along_y(axis_coord_: int):
    global height
    for coord_ in filter(lambda p: p[1] == axis_coord_, points):
        points.remove(coord_)

    for x_, y_ in product(range(width), range(axis_coord_)):
        other_point = (x_, height-y_-1)
        if other_point not in points:
            continue
        points.add((x_, y_))
        points.remove(other_point)
    height = axis_coord_


axis, coord = folds[0]
if axis == 'x':
    fold_along_x(coord)
elif axis == 'y':
    fold_along_y(coord)
else:
    raise Exception()

# print_points()
print(len(points))
