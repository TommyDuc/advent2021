#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


class Entry:
    def __init__(self, line: str):
        left_right = line.split('|')
        self.samples = list(map(lambda x: set(x), left_right[0].split()))
        self.displays = list(map(lambda x: set(x), left_right[1].split()))
        pass


entries = list(map(lambda line: Entry(line), input_))

answer = 0
for entry in entries:
    displays_1 = list(filter(lambda x: len(x) == 2, entry.displays))
    displays_4 = list(filter(lambda x: len(x) == 4, entry.displays))
    displays_7 = list(filter(lambda x: len(x) == 3, entry.displays))
    displays_8 = list(filter(lambda x: len(x) == 7, entry.displays))

    answer += len(displays_1)
    answer += len(displays_4)
    answer += len(displays_7)
    answer += len(displays_8)

print(answer)
