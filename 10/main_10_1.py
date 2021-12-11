#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

openings = list('([{<')
closings = list(')]}>')
open_close_lookup = dict(zip(openings, closings))
bracket_points_lookup = dict(zip(closings, [3, 57, 1197, 25137]))


def get_last_wrong_bracket(line_: str):
    stack = []
    for c in line_:
        if c in openings:
            stack.append(c)
        elif c in closings:
            corresponding = stack.pop()
            if open_close_lookup[corresponding] != c:
                return c
        else:
            raise Exception()
    return None


answer = 0
for line in input_:
    wrong = get_last_wrong_bracket(line)
    if wrong is not None:
        answer += bracket_points_lookup[wrong]

print(answer)
