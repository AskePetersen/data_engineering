import operator
import re
from functools import reduce
from math import fmod

import cv2
import numpy as np
from matplotlib import pyplot as plt


def print_positions(posses, b, h):
    mapper = np.zeros((b, h), dtype=int)
    for x, y in posses:
        mapper[int(x), int(y)] += 1
    print(mapper.T)


def save_map(posses, b, h, s):
    bitmap = np.zeros((b, h), dtype=np.uint8)
    for x, y in posses:
        bitmap[int(x), int(y)] = 255
    cv2.imwrite(f"bitmap{s}.png", bitmap)


def solv2(puzzle_input, b, h):
    lines = puzzle_input.split("\n")
    secs = 6
    res = 0
    for s in range(5, secs):
        posses = []
        for line in lines[:-1]:
            pos_vel = list(map(int, re.findall(r"-?\d+", line)))
            init_x = pos_vel[0]
            init_y = pos_vel[1]
            Vx = pos_vel[2]
            Vy = pos_vel[3]

            raw_x = fmod((init_x + Vx * s), b)
            raw_y = fmod((init_y + Vy * s), h)
            x = raw_x if raw_x >= 0 else b + raw_x
            y = raw_y if raw_y >= 0 else h + raw_y
            posses.append((x, y))
        print_positions(posses, b, h)
        quit()
        save_map(posses, b, h, s)


def solv1(puzzle_input, b, h):
    lines = puzzle_input.split("\n")
    secs = 100
    res = 0
    posses = []
    quad_values = [0, 0, 0, 0]
    for line in lines[:-1]:
        pos_vel = list(map(int, re.findall(r"-?\d+", line)))
        init_x = pos_vel[0]
        init_y = pos_vel[1]
        Vx = pos_vel[2]
        Vy = pos_vel[3]

        raw_x = fmod((init_x + Vx * secs), b)
        raw_y = fmod((init_y + Vy * secs), h)
        x = raw_x if raw_x >= 0 else b + raw_x
        y = raw_y if raw_y >= 0 else h + raw_y
        x_thresh = b // 2
        y_thresh = h // 2
        if x != x_thresh and y != y_thresh:
            idx = 0 if x < x_thresh else 1
            idx += 2 if y > x_thresh else 0
            quad_values[idx] += 1
    print(reduce(operator.mul, quad_values, 1))


if __name__ == "__main__":
    file = "test"
    if file == "test":
        b = 11
        h = 7
    else:
        b = 101
        h = 103
    with open(file) as f:
        puzzle_input = f.read()
    solv2(puzzle_input, b, h)
