#!/usr/bin/env python3

from itertools import product
from typing import List
import os
import sys


class Square:
    def __init__(self, value: int = None, group: int = None):
        self.value = value
        self.group = group


class Group:
    def __init__(self, group_id: int):
        self.id = group_id
        self.count = 0


with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

nines_count = 0
squares: List[List[Square]] = list()
for line in input_:
    row = list()
    squares.append(row)
    for number in [int(i) for i in line if i != '\n']:
        row.append(Square(number, None))
        nines_count += 1 if number == 9 else 0
height, width = len(squares), len(squares[0])
square_to_visit = sum(map(lambda x: len(x), squares)) - nines_count

group_counter = 0
groups = list()


def find_starting_position_for_new_group():
    for i_, j_ in product(range(height), range(width)):
        if squares[i_][j_].value != 9 and squares[i_][j_].group is None:
            return i_, j_


sys.setrecursionlimit(height+width)


def find_group(i_, j_, group: Group):
    current = squares[i_][j_]

    if current.value == 9:
        return

    current.group = group_counter
    group.count += 1

    if i_ != 0 and squares[i_ - 1][j_].group is None and squares[i_ - 1][j_].value != 9:
        find_group(i_ - 1, j_, group)
    if i_ != height-1 and squares[i_ + 1][j_].group is None and squares[i_ + 1][j_].value != 9:
        find_group(i_ + 1, j_, group)
    if j_ != 0 and squares[i_][j_ - 1].group is None and squares[i_][j_ - 1].value != 9:
        find_group(i_, j_ - 1, group)
    if j_ != width-1 and squares[i_][j_ + 1].group is None and squares[i_][j_ + 1].value != 9:
        find_group(i_, j_ + 1, group)


while sum(map(lambda x: x.count, groups)) != square_to_visit:
    current_group = Group(group_counter)
    i, j = find_starting_position_for_new_group()
    find_group(i, j, current_group)
    groups.append(current_group)
    group_counter += 1

groups.sort(key=lambda g: g.count, reverse=True)
answer = 1
for group in groups[:3]:
    answer *= group.count
print(answer)

