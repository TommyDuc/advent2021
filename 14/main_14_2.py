#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    first_chain = file.readline().strip()
    file.readline()
    insertion_rules_lines = [line.strip() for line in file.readlines() if line]

pair_insertion_rules = dict()
rules_count = dict()
characters = set(first_chain)
for insertion_rule_line in insertion_rules_lines:
    pair, _, insertion = insertion_rule_line.split()
    pair_insertion_rules[pair] = insertion
    rules_count[pair] = 0
    characters |= set(pair) | set(insertion)

for c1, c2 in zip(first_chain[0:-1], first_chain[1:]):
    rules_count[c1 + c2] += 1
chars_count = dict.fromkeys(characters, 0)
for c in first_chain:
    chars_count[c] += 1

generation_count = 40
for generation in range(1, generation_count+1):
    new_rules_count = dict.fromkeys(rules_count.keys(), 0)
    for pair, count in rules_count.items():
        if count == 0:
            continue
        inserted_char = pair_insertion_rules[pair]
        chars_count[inserted_char] += count
        new_pair1 = pair[0] + inserted_char
        new_pair2 = inserted_char + pair[1]
        new_rules_count[new_pair1] += count
        new_rules_count[new_pair2] += count
    rules_count = new_rules_count

characters_counter_sorted = list(chars_count.items())
characters_counter_sorted.sort(key=lambda x: x[1])
answer = characters_counter_sorted[-1][1] - characters_counter_sorted[0][1]
print(answer)
