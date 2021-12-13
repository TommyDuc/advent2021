#!/usr/bin/env python3

import re
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


def append(path_: tuple[str], node_id: str) -> tuple[str]:
    if not re.match(r"[A-Z]+", node_id) and node_id in path_:
        return None
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
    current_path = next(iter(wip_paths))
    explore_path(current_path)


print(len(finished_paths))
