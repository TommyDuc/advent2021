#!/usr/bin/env python3

import os
import re
import math
from itertools import product

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.readline().strip()

limits = re.findall(r"(-?\d+)", input_)
x0, x1, y0, y1 = map(lambda x: int(x), limits)
x_range = list(range(x0, x1 + 1))
y_range = list(range(y0, y1 + 1))


def y_i(i_, vy_):
    # This equation accounts for the speed decreasing *after* the first step
    y_ = i_ * vy_ + int(0.5 * i_ * (1 - i_))
    return y_


def i_y(y_, vy_):
    # Using quadratic equation. Multiplied by 2/2 to remove fractions
    discriminant = (2*vy_+1)**2 - 8*y_
    if discriminant < 0:
        return []
    square_root = math.sqrt(discriminant)
    if not square_root.is_integer():
        return []

    return_i = list()
    left_part = 2*vy_ + 1
    first, second = (left_part + square_root)/2, (left_part - square_root)/2
    if first >= 0 and first.is_integer():
        return_i.append(int(first))
    if second >= 0 and second.is_integer():
        return_i.append(int(second))
    return return_i


def i_range_y(y_, vy_):
    # Using quadratic equation. Multiplied by 2/2 to remove fractions
    discriminant = (2*vy_+1)**2 - 8*y_
    if discriminant < 0:
        return []
    square_root = math.sqrt(discriminant)

    return_i = list()
    left_part = 2*vy_ + 1
    first, second = (left_part + square_root)/2, (left_part - square_root)/2
    if first >= 0:
        return_i.append(first)
    if second >= 0:
        return_i.append(second)
    return_i.sort()
    return return_i


def i_max(vy_):
    # Calculated by solving 0=dy/di for i
    i_max_precise = 0.5 + vy_
    return int(i_max_precise), int(i_max_precise)+1


def x_i(i_, vx_):
    if i_ >= vx_:
        return y_i(vx_-1, vx_)
    return y_i(i_, vx_)


def speeds_are_in_square(vx_, vy_):
    # First we get the possible steps to test
    possible_steps = list()
    possible_steps.extend(i_range_y(y0, vy_))
    possible_steps.extend(i_range_y(y1, vy_))
    possible_steps.sort()
    if not possible_steps:
        return False

    first_step, last_step = int(possible_steps[0]), int(possible_steps[-1]) + 1
    for i in range(first_step, last_step+1):
        computed_x = x_i(i, vx_)
        computed_y = y_i(i, vy_)
        if computed_x in x_range and computed_y in y_range:
            return True
    return False


# We must first limit the speeds search space
vx_min = int(0.5*(-1+math.sqrt(1+8*x0)))  # Must at least reach the first x of the target
vx_max = x1  # Must not go beyond the target after the first step
vy_min = y0  # Must not go beyond the target after the first step
vy_max = -y0+1  # Vertical speed is symmetric but one step in advance

speed_count = 0
for vx, vy in product(range(vx_min, vx_max+1), range(vy_min, vy_max+1)):
    if speeds_are_in_square(vx, vy):
        speed_count += 1

print(speed_count)
