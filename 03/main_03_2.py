#!/usr/bin/env python3

import copy
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

# input_ = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def get_select_bit(lines, index, func):
    column = ""
    for line in lines:
        column += line[index]

    number_of_ones = column.count("1")
    number_of_zeroes = column.count("0")
    return func(number_of_ones, number_of_zeroes)


def get_data(select_func):
    candidates = copy.copy(input_)
    for bit_index in range(len(input_[0])):
        select_bit = get_select_bit(candidates, bit_index, select_func)
        candidates = list(filter(lambda candidate_str: select_bit == candidate_str[bit_index], candidates))
        if len(candidates) == 1:
            break
    return int(candidates[0], base=2)


oxygen = get_data(lambda ones, zeroes: "1" if ones >= zeroes else "0")
c02 = get_data(lambda ones, zeroes: "0" if ones >= zeroes else "1")
print(oxygen * c02)
