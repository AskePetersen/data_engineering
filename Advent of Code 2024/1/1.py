import re

import numpy as np


def part1(input):
    lines = input.split("\n")
    fst = []
    snd = []
    lines = [l for l in lines if l]
    for line in lines:
        pls = re.findall(r"(\d+)   (\d+)", line)

        a, b = map(int, pls[0])

        fst.append(int(a))
        snd.append(int(b))
    fst = sorted(fst)
    snd = sorted(snd)
    res = sum([abs(f - s) for f, s in zip(fst, snd)])
    return res


def part2(input):
    lines = input.split("\n")
    fst = []
    snd = []
    lines = [l for l in lines if l]
    for line in lines:
        pls = re.findall(r"(\d+)   (\d+)", line)

        a, b = map(int, pls[0])

        fst.append(int(a))
        snd.append(int(b))

    counter = np.zeros(max(max(fst), max(snd)) + 1)
    for ele in snd:
        counter[ele] += 1
    res = 0
    for ele in fst:
        res += ele * counter[ele]
    print(counter)
    return res


if __name__ == "__main__":
    file = "input"
    with open(file) as f:
        input = f.read()
    print(part2(input))
