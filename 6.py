#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B2", "D2", "F2", "H2", "J2", "L2", "N2",
             "B3", "D3", "F3", "H3", "J3",
             "B4", "D4", "F4", "H4", "L4", "M4", "N4",
             "B5", "D5", "F5",
             "B6", "D6", "K6", "L6", "M6", "N6",
             "B7",
             "J8", "K8", "L8", "M8", "N8"}


def move(position, direction):
    i = XAXIS.index(position[0])
    j = YAXIS.index(position[1])
    if direction == "left":
        if i > 0:
            return XAXIS[i - 1] + position[1]
    elif direction == "right":
        if i < len(XAXIS) - 1:
            return XAXIS[i + 1] + position[1]
    elif direction == "up":
        if j > 0:
            return position[0] + YAXIS[j - 1]
    elif direction == "down":
        if j < len(YAXIS) - 1:
            return position[0] + YAXIS[j + 1]


def can_move(position, direction):
    if position[0] == XAXIS[0] and direction == "left":
        return False
    elif position[0] == XAXIS[-1] and direction == "right":
        return False
    elif position[1] == YAXIS[0] and direction == "up":
        return False
    elif position[1] == YAXIS[-1] and direction == "down":
        return False
    new_position = move(position, direction)
    return new_position not in FORBIDDEN


def execute(start):
    position = start

    while can_move(position, "left"):
        position = move(position, "left")
    while can_move(position, "right"):
        position = move(position, "right")
    if can_move(position, "up"):
        position = move(position, "up")
    else:
        return False
    if can_move(position, "right"):
        return True
    else:
        return False


if __name__ == "__main__":
    result = 0
    for x in XAXIS:
        for y in YAXIS:
            position = x + y
            if position in FORBIDDEN:
                continue
            if execute(position):
                result += 1
    print(result)