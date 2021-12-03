#!/usr/bin/env python3

import copy
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

# input_ = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

bin_length = len(input_[0])


def get_select_bit(lines, index, func):
    column = ""
    for line in lines:
        column += line[index]

    number_of_ones = column.count("1")
    number_of_zeroes = column.count("0")
    return func(number_of_ones, number_of_zeroes)


oxygen_candidates = copy.deepcopy(input_)
for i in range(bin_length):
    criteria_bit = get_select_bit(oxygen_candidates, i, lambda ones, zeroes: "1" if ones >= zeroes else "0")
    oxygen_candidates = list(filter(lambda candidate_str: criteria_bit == candidate_str[i], oxygen_candidates))
    if len(oxygen_candidates) == 1:
        break

c02_candidates = copy.deepcopy(input_)
for i in range(bin_length):
    criteria_bit = get_select_bit(c02_candidates, i, lambda ones, zeroes: "0" if ones >= zeroes else "1")
    c02_candidates = list(filter(lambda candidate_str: criteria_bit == candidate_str[i], c02_candidates))
    if len(c02_candidates) == 1:
        break

oxygen = int(oxygen_candidates[0], base=2)
c02 = int(c02_candidates[0], base=2)
print(oxygen * c02)
