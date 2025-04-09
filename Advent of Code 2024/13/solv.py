# USE CRAMERS RULE FOR 2x2 MATRICES
import re

import numpy as np


# A  B
def compute_det(X):  #         C  D
    a, b, c, d = X
    det = a * d - (c * b)
    return det


def compute_dx_dy(X, Y, det):
    Dx = compute_det([Y[0], X[1], Y[1], X[3]])
    Dy = compute_det([X[0], Y[0], X[2], Y[1]])
    x = Dx/det
    y = Dy/det
    return x, y


def solv1(puzzle_input):
    segments = puzzle_input.split("\n\n")
    res = 0

    for seg in segments:
        n = re.findall(r"\d+", seg)
        n = list(map(int, n))
        X = [n[0], n[2], n[1], n[3]]
        det = compute_det(X)
        Y = [n[4]+ 10000000000000, n[5]+10000000000000]
        x, y = compute_dx_dy(X, Y, det)
        if x.is_integer() and y.is_integer():
            res += x*3 + y

    print(res)


if __name__ == "__main__":
    file = "input"
    with open(file, "r") as f:
        puzzle_input = f.read()
    solv1(puzzle_input)
