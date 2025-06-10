def part1(input):
    input = input.split("\n")

    res = 0
    for line in input:
        lvl = list(map(int, line.split(" ")))
        status = ""
        if lvl[0] > lvl[1]:
            status = "dec"
        else:
            status = "inc"
        tmp = lvl[0]

        for i, ele in enumerate(lvl[1:]):
            if abs(tmp - ele) > 3:
                break
            if status == "dec" and tmp < ele:
                break
            if status == "inc" and tmp > ele:
                break
            if tmp == ele:
                break
            if i == len(lvl) - 2:
                res += 1
            tmp = ele

    return res


def part2(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


data = [[int(y) for y in x.split(" ")] for x in open("input").read().split("\n")[:-1]]

safe_count = sum([part2(row) for row in data])
print(safe_count)

safe_count = sum(
    [any([part2(row[:i] + row[i + 1 :]) for i in range(len(row))]) for row in data]
)
print(safe_count)
