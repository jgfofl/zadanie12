#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B2","C2","D2","E2","I2","J2","K2","L2","M2",
             "B3","I3",
             "B4","F4","H4","I4","K4","N4",
             "B5","F5","H5","K5","N5",
             "B6","F6","H6","K6","N6","O6",
             "C7","F7","K7",
             "C8","K8"}

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
