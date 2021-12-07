#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = file.read().split(',')

generations = 256
fishes = list(map(lambda f: int(f), input_))

# Because functools.cache decorator is new in version 3.9
cache = dict()


def get_spawned_fishes(fish_, remaining_generations):
    if (fish_, remaining_generations) in cache:
        return cache[(fish_, remaining_generations)]

    if remaining_generations <= 0:
        return 1

    spawn_count = 0

    if fish_ == 0:
        spawn_count += get_spawned_fishes(8, remaining_generations - 1)
        spawn_count += get_spawned_fishes(6, remaining_generations - 1)
    else:
        spawn_count += get_spawned_fishes(fish_ - 1, remaining_generations - 1)

    cache[(fish_, remaining_generations)] = spawn_count
    return spawn_count


total_fishes = 0
for fish in fishes:
    total_fishes += get_spawned_fishes(fish, generations)

print(total_fishes)
