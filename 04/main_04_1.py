#!/usr/bin/env python3

import numpy as np
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    called_numbers = [int(i) for i in file.readline().split(',')]
    file.readline()
    input_ = file.read()


def is_won(bingo_card_, called_numbers_so_far):
    for row in bingo_card_:
        if set(row).issubset(called_numbers_so_far):
            return True
    for column in bingo_card_.T:
        if set(column).issubset(called_numbers_so_far):
            return True
    return False


bingo_cards = list()
for bingo_str in input_.split('\n\n'):
    bingo_str.replace('\n', ' ')
    numbers = [int(i) for i in bingo_str.split()]
    bingo_card = np.array(numbers)
    bingo_card.resize((5, 5))
    bingo_cards.append(bingo_card)


numbers_called = set()
for called_number in called_numbers:
    numbers_called.add(called_number)
    for bingo_card in bingo_cards:
        if is_won(bingo_card, numbers_called):
            bingo_card.resize((1, 25))
            all_card_numbers = set(bingo_card[0])
            unmarked = all_card_numbers - numbers_called
            print(sum(unmarked) * called_number)
            exit(0)
