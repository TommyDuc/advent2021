#!/usr/bin/env python3

from typing import List
import os

with open(f"{os.path.dirname(__file__)}/input", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

openings = set('([{<')
closings = set(')]}>')
open_close_lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}
close_open_lookup = dict(zip(open_close_lookup.values(), open_close_lookup.keys()))
bracket_points_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}


class Node:
    id_counter = 0

    def __init__(self, parent=None, opening="", closing=""):
        self.parent = parent
        self.children: List[Node] = list()
        self.opening: str = opening
        self.closing: str = closing
        self.id = Node.id_counter
        Node.id_counter += 1

    def is_valid(self):
        is_nod_valid = self.closing == open_close_lookup[self.opening]
        for child in self.children:
            is_nod_valid &= child.is_valid()
        return is_nod_valid


def print_node(node: Node, level: int = 0):
    print(level*"\t" + node.opening)
    for child in node.children:
        print_node(child, level+1)
    print(level*"\t" + node.closing)


# Oh, well, it was fun to code #nostalgia
def get_ast_tree(line: str):
    root_ = current_node = Node(parent=None, opening=line[0])
    nodes_ = [root_]
    for c in line[1:]:
        if c in openings:
            new_node = Node(parent=current_node, opening=c)
            nodes_.append(new_node)
            current_node.children.append(new_node)
            current_node = new_node
        elif c in closings:
            current_node.closing = c
            if current_node.parent is not None:
                current_node = current_node.parent
        else:
            raise Exception()
    return root_, nodes_


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
