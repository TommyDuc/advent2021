#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

openings = list('([{<')
closings = list(')]}>')
open_close_lookup = dict(zip(openings, closings))
bracket_points_lookup = dict(zip(closings, [1, 2, 3, 4]))


def get_completion_brackets(line_: str):
    stack = []
    for c in line_:
        if c in openings:
            stack.append(c)
        elif c in closings:
            corresponding = stack.pop()
            if open_close_lookup[corresponding] != c:
                return []
        else:
            raise Exception()

    completion_brackets_ = list(map(lambda x: open_close_lookup[x], reversed(stack)))
    return completion_brackets_


def get_score(completion_brackets_):
    score = 0
    for c in completion_brackets_:
        score *= 5
        score += bracket_points_lookup[c]
    return score


scores = list()
for line in input_:
    completion_brackets = get_completion_brackets(line)
    if completion_brackets:
        scores.append(get_score(completion_brackets))

scores.sort()
answer = scores[int(len(scores)/2)]
print(answer)
