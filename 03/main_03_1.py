#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

bin_length = len(input_[0])

columns = list()
for i in range(bin_length):
    columns.append("")
    for line in input_:
        columns[i] += line[i]

gamma_str = ""
epsilon_str = ""

for column in columns:
    number_of_ones = column.count("1")
    number_of_zeroes = column.count("0")
    gamma_str += "1" if number_of_ones > number_of_zeroes else "0"
    epsilon_str += "0" if number_of_ones > number_of_zeroes else "1"

gamma = int(gamma_str, base=2)
epsilon = int(epsilon_str, base=2)
print(gamma*epsilon)
