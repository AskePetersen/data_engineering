import math
import sys
from itertools import product


def process(combinations, n_ops, nums, tar):
    for c in combinations:
        res = nums[0]
        for i in range(n_ops):
            if c[i] == "+":
                res += nums[i + 1]
            else:
                res *= nums[i + 1]
        if res == tar:
            return res
    return 0

def process2(combinations, n_ops, nums, tar):
    for c in combinations:
        res = nums[0]
        for i in range(n_ops):
            if c[i] == "+":
                res += nums[i + 1]
            elif c[i] == "*":
                res *= nums[i + 1]
            elif c[i] == "||":
                res_str = str(res) + str(nums[i + 1])
                res = int(res_str)
            else:
                print("error")
                quit()

        if res == tar:
            return res
    return 0


def part1():
    file = "test"
    result = 0
    for l in sys.stdin:
        data = l.strip()

        tar, nums = data.split(": ")
        tar = int(tar)
        nums = list(map(int, nums.split(" ")))
        n_ops = len(nums) - 1
        combinations = list(product(["+", "*"], repeat=n_ops))
        result += process(combinations, n_ops, nums, tar)

    print(result)


def part2():
    file = "test"
    result = 0
    for l in sys.stdin:
        data = l.strip()

        tar, nums = data.split(": ")
        tar = int(tar)
        nums = list(map(int, nums.split(" ")))
        n_ops = len(nums) - 1
        combinations = list(product(["+", "*", "||"], repeat=n_ops))
        result += process2(combinations, n_ops, nums, tar)
    print(result)
part2()
