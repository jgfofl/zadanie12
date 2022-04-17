#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing as t


XAXIS: t.Final[str] = "ABCDEFGHIJKLMNO"
YAXIS: t.Final[str] = "12345678"

FORBIDDEN: t.Final[t.Set[str]] = {
    "K1",
    "K2",
    "C3", "D3", "E3", "F3", "G3", "H3", "K3", "M3",
    "B4", "I4", "M4",
    "B5", "M5",
    "B6", "C6", "J6", "K6", "M6",
    "D7", "E7", "H7", "I7",
    "D8", "E8", "H8", "I8",
}


def move(position: str, direction: str) -> str:
    i = XAXIS.index(position[0])
    j = YAXIS.index(position[1])

    if direction == "left":
        if i > 0:
            return XAXIS[i - 1] + position[1]

    elif direction == "right":
        if i < len(XAXIS) - 1:
            return XAXIS[i + 1] + position[1]

    elif direction == "down":
        if j < len(YAXIS) - 1:
            return position[0] + YAXIS[j + 1]

    elif direction == "up":
        if j > 0:
            return position[0] + YAXIS[j - 1]

    return position


def can_move(position: str, direction: str) -> bool:
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


def execute(start: str) -> bool:
    position = start
    while can_move(position, "down"):
        position = move(position, "down")

    while can_move(position, "right"):
        position = move(position, "right")

    if can_move(position, "up"):
        position = move(position, "up")
    else:
        return False

    return can_move(position, "right")


if __name__ == "__main__":
    result = 0

    for x in XAXIS:
        for y in YAXIS:
            current = x + y
            if current in FORBIDDEN:
                continue

            if execute(current):
                result += 1

    print(result)
