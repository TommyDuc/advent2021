#!/usr/bin/env python3

import re
import os
from collections import Counter

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

lower_regex = re.compile(r"[a-z]+")


def get_counts(iterable_) -> dict:
    set_ = set(iterable_)
    counter = Counter(iterable_)
    counts_ = dict()
    for c in set_:
        counts_[c] = counter[c]
    return counts_


def append(path_: tuple[str], node_id: str) -> tuple[str]:
    if node_id in ['start', 'end'] and node_id in path_:
        return tuple()
    if lower_regex.match(node_id):
        small_list = list(filter(lambda n: lower_regex.match(n), path_))
        counts = get_counts(small_list)
        has_a_small_twice = max(counts.values()) >= 2
        if has_a_small_twice and node_id in small_list:
            return tuple()
        if node_id in small_list and counts[node_id] >= 2:
            return tuple()
    return tuple([*path_, node_id])


links: [dict[str, str]] = dict()
for line in input_:
    from_, to_ = line.split('-')
    if from_ not in links:
        links[from_] = list()
    if to_ not in links:
        links[to_] = list()
    links[from_].append(to_)
    links[to_].append(from_)

wip_paths: set[tuple[str]] = {tuple(['start'])}
finished_paths: set[tuple[str]] = set()


def explore_path(path_: tuple[str]):
    node_from = path_[-1]
    for node_to in links[node_from]:
        if new_path := append(path_, node_to):
            if node_to == "end":
                finished_paths.add(new_path)
            else:
                wip_paths.add(new_path)
    wip_paths.remove(path_)


while wip_paths:
    explore_path(next(iter(wip_paths)))

print(len(finished_paths))
