#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B2","C2","D2","E2","F2",
             "D3","E3","F3","G3",
             "F4","G4","H4",
             "H5","I5","L5","M5",
             "D6","J6","K6","L6",
             "B7","H7","I7","J7","K7",
             "F8","G8","H8","I8","J8"}

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
    if can_move(position, "left"):
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