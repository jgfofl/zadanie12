#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B1","C1","H1","O1",
             "C2","H2","O2",
             "C3","F3","G3","H3","I3","J3","M3",
             "B4","C4","M4",
             "C5","G5","H5","J5","K5","L5","M5","N5",
             "G6","H6","L6",
             "B7","E7","G7","H7","L7",
             "B8","G8","H8","L8",}

def move(position, direction):
    i = XAXIS.index(position[0])
    j = YAXIS.index(position[1])
    if direction == "left":
        if i > 0:
            return XAXIS[i-1] + position[1]
    elif direction == "right":
        if i < len(XAXIS) - 1:
            return XAXIS[i+1] + position [1]
    elif direction == "up":
        if j > 0:
            return position[0] + YAXIS[j-1]
    elif direction == "down":
        if j < len(YAXIS) - 1:
            return position[0] + YAXIS[j+1]


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
    while can_move(position, "up"):
        position = move(position, "up")
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
            position = x+y
            if position in FORBIDDEN:
                continue
            if execute(position):
                result+=1
    print(result)
