#!/usr/bin/env python3

import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

#                   aaaa
#                  b    c
#                  b    c
#                   dddd
#                  e    f
#                  e    f
#                   gggg

#          0:      1:      2:      3:      4:
#         aaaa    ....    aaaa    aaaa    ....
#        b    c  .    c  .    c  .    c  b    c
#        b    c  .    c  .    c  .    c  b    c
#         ....    ....    dddd    dddd    dddd
#        e    f  .    f  e    .  .    f  .    f
#        e    f  .    f  e    .  .    f  .    f
#         gggg    ....    gggg    gggg    ....
#
#          5:      6:      7:      8:      9:
#         aaaa    aaaa    aaaa    aaaa    aaaa
#        b    .  b    .  .    c  b    c  b    c
#        b    .  b    .  .    c  b    c  b    c
#         dddd    dddd    ....    dddd    dddd
#        .    f  e    f  .    f  e    f  .    f
#        .    f  e    f  .    f  e    f  .    f
#         gggg    gggg    ....    gggg    gggg

all_segments = set('abcdefg')

# I could use this to refactor some stuff, if I have time, maybe, eventually...
number_segments_known_by_length = {
    "1": set('cf'),
    "4": set('bcdf'),
    "7": set('bcdf'),
    "8": set('abcdefg'),
    "235": set('adg'),
    "069": set('abfg')
}

segments_number_truth_table = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}


def remove_known_connections(signal_segments):
    single_letters = set()
    for segment in signal_segments.values():
        if len(segment) == 1:
            single_letters.add(list(segment)[0])

    for key in signal_segments.keys():
        if len(signal_segments[key]) > 1:
            signal_segments[key].difference_update(single_letters)


def get_possible_numbers(display_segments, signal_segments_):
    n_segment = len(display_segments)
    if n_segment == 2:
        return {1}
    if n_segment == 4:
        return {4}
    if n_segment == 3:
        return {7}
    if n_segment == 7:
        return {8}

    return {0, 2, 3, 5, 6, 9}


def get_candidate_number(display, signal_segments):
    candidates = set()

    # Everything is suffering; 3:30AM edition.
    # But seriously, I have no idea how to do this without this lovely waterfall. Forgive me Uncle Bob sempai.
    # This could be done if possible segments were of the same length and we could just use zip and some
    # permutation algorithm. Simply looping over all letters and candidates won't either since we need
    # the current candidate of the signals at the same time.
    for a_ in signal_segments["a"]:
        for b_ in signal_segments["b"]:
            for c_ in signal_segments["c"]:
                for d_ in signal_segments["d"]:
                    for e_ in signal_segments["e"]:
                        for f_ in signal_segments["f"]:
                            for g_ in signal_segments["g"]:
                                translation_dict = {a_: "a", b_: "b", c_: "c", d_: "d", e_: "e", f_: "f", g_: "g"}
                                translated_display = []
                                for char in display:
                                    if char not in translation_dict:
                                        translated_display = []
                                        break
                                    else:
                                        translated_char = translation_dict[char]
                                        translated_display.append(translated_char)
                                translated_display.sort()
                                translated_display = "".join(translated_display)
                                if translated_display and translated_display in segments_number_truth_table:
                                    candidates.add(segments_number_truth_table[translated_display])

    return candidates


def get_numbers(line: str):
    display_numbers_returned = [None]*4

    left_right = line.split('|')
    samples = list(map(lambda x: set(x), left_right[0].split()))
    displays = list(map(lambda x: set(x), left_right[1].split()))

    signal_segments = dict()
    for key in all_segments:
        signal_segments[key] = set(all_segments)

    signals_1 = next(filter(lambda x: len(x) == 2, samples))
    signals_4 = next(filter(lambda x: len(x) == 4, samples))
    signals_7 = next(filter(lambda x: len(x) == 3, samples))
    signals_8 = next(filter(lambda x: len(x) == 7, samples))
    signals_235 = next(filter(lambda x: len(x) == 5, samples))
    signals_069 = next(filter(lambda x: len(x) == 6, samples))

    for key in 'cf':
        signal_segments[key].intersection_update(signals_1)
    for key in 'bcdf':
        signal_segments[key].intersection_update(signals_4)
    for key in 'acf':
        signal_segments[key].intersection_update(signals_7)
    for key in 'abcdefg':
        signal_segments[key].intersection_update(signals_8)
    for key in 'adg':
        signal_segments[key].intersection_update(signals_235)
    for key in 'abfg':
        signal_segments[key].intersection_update(signals_069)

    for key in all_segments - set('cf'):
        signal_segments[key].difference_update(signals_1)
    for key in all_segments - set('bcdf'):
        signal_segments[key].difference_update(signals_4)
    for key in all_segments - set('acf'):
        signal_segments[key].difference_update(signals_7)
    for key in all_segments - set('abcdefg'):
        signal_segments[key].difference_update(signals_8)  # This should never execute

    it_count = 0
    while None in display_numbers_returned and it_count < 10:
        it_count += 1
        remove_known_connections(signal_segments)

        for i, display in enumerate(displays):
            possible_numbers = get_possible_numbers(display, signal_segments)
            deduced_numbers = get_candidate_number(display, signal_segments)
            if len(possible_numbers) == 1:
                display_numbers_returned[i] = list(possible_numbers)[0]
            elif len(deduced_numbers) == 1:
                display_numbers_returned[i] = list(deduced_numbers)[0]

    return display_numbers_returned


numbers_arr = list(map(get_numbers, input_))
answer = 0
for number_arr in numbers_arr:
    # For some reason int("".join(number_arr)) doesn't work.
    n3, n2, n1, n0 = number_arr
    n = n3*1000 + n2*100 + n1*10 + n0
    answer += n
print(answer)
