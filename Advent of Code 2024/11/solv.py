# USE DYNAMIC PROGRAMMING WITH MEMOIZATION
from functools import cache
from math import floor, log10


def count(x, d=75):
    if d == 0:
        return 1
    if x == 0:
        return count(1, d - 1)

    l = floor(log10(x)) + 1
    if l % 2:
        return count(x * 2024, d - 1)

    return count(x // 10 ** (l // 2), d - 1) + count(x % 10 ** (l // 2), d - 1)


@cache
def solv1(input):
    dic = {}
    lst = input[0].split(" ")
    for i in range(75):
        print(i)
        new_lst = []
        for ele in lst:
            if ele in list(dic.keys()):
                new_lst.append(dic[ele])
                continue
            if ele == "0":
                dic[ele] = "1"
            elif len(ele) % 2 == 0:
                new_lst.append(str(int(ele[: len(ele) // 2])))
                new_lst.append(str(int(ele[len(ele) // 2 :])))
                continue
            else:
                dic[ele] = str(int(ele) * 2024)
            new_lst.append(dic[ele])

        lst = new_lst
    return len(lst)


if __name__ == "__main__":
    file = "input"

    with open(file) as f:
        lines = [ele.strip() for ele in f.readlines()]

    res = solv1(lines)
    print(res)

    data = map(int, lines[0].split())
    print(sum(map(count, data)))
