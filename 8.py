#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B1", "C1", "D1", "L1", "M1", "N1",
             "B3", "C3", "D3", "E3", "F3", "J3", "K3", "L3", "M3", "N3",
             "E4", "K4",
             "D5", "L5",
             "C6", "M6",
             "B7", "C7", "D7", "E7", "F7", "J7", "K7", "L7", "M7", "N7", }


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

    while can_move(position, "down"):
        position = move(position, "down")
    while can_move(position, "left"):
        position = move(position, "left")
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
