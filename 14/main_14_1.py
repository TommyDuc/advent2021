#!/usr/bin/env python3

import os
from collections import Counter

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    chain = file.readline().strip()
    file.readline()
    insertion_rules_lines = [line.strip() for line in file.readlines() if line]

pair_insertion_rules = dict()
for insertion_rule_line in insertion_rules_lines:
    pair, _, insertion = insertion_rule_line.split()
    pair_insertion_rules[pair] = insertion

for _ in range(10):
    new_chain = chain
    for i, pair_tuple in enumerate(zip(chain[0:-1], chain[1:])):
        pair = pair_tuple[0] + pair_tuple[1]
        if pair in pair_insertion_rules:
            offset = len(new_chain) - len(chain)
            new_chain = new_chain[0:i+1+offset] + pair_insertion_rules[pair] + new_chain[i+1+offset:]

    chain = new_chain

chain_counter = Counter(chain)
characters = set(chain)
characters_counter_sorted = list(chain_counter.items())
characters_counter_sorted.sort(key=lambda x: x[1])
answer = characters_counter_sorted[-1][1] - characters_counter_sorted[0][1]
print(answer)
