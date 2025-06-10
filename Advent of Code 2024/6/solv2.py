def part2():
    file = "input"
    with open(file) as f:
        data = f.read().strip().split("\n")

    x, y = 0, 0
    arrs = []
    test = []
    for i, line in enumerate(data):
        arrs.append([[char] for char in line])
        test.append(list(line))

        for j, char in enumerate(line):
            if char == "^":
                x, y = i, j

    res = 0
    while True:

        # up
        while "#" not in arrs[x][y] and x < len(arrs) - 1:
            arrs[x][y].append("u")
            x = x + 1
        x = x - 1
        while "#" not in arrs[x][y]:
            arrs[x][y].append("u")
            if "r" in arrs[x][y]:
                test[x - 1][y] = "O"
                res += 1
            arrs[x][y].append("u")
            x = x - 1
            if x < 0:
                return res, arrs, test

        x = x + 1

        # right
        while "#" not in arrs[x][y] and y >= 0:
            arrs[x][y].append("r")
            y = y - 1
        y = y + 1
        while "#" not in arrs[x][y]:
            if "d" in arrs[x][y]:
                test[x][y + 1] = "O"
                res += 1
            arrs[x][y].append("r")
            y = y + 1
            if y >= len(arrs[0]):
                return res, arrs, test
        y = y - 1

        # down
        while "#" not in arrs[x][y] and x >= 0:
            arrs[x][y].append("d")
            x = x - 1
        x = x + 1
        while "#" not in arrs[x][y]:
            if "l" in arrs[x][y]:
                test[x + 1][y] = "O"
                res += 1
            arrs[x][y].append("d")
            x = x + 1
            if x >= len(arrs):
                return res, arrs, test
        x = x - 1

        # left
        while "#" not in arrs[x][y] and y < len(arrs[0]) - 1:
            arrs[x][y].append("l")
            y = y + 1
        y = y - 1
        while "#" not in arrs[x][y]:
            if "u" in arrs[x][y]:
                test[x][y - 1] = "O"
                res += 1
            arrs[x][y].append("l")
            y = y - 1
            if y < 0:
                return res, arrs, test
        y = y + 1


res, arrs, test = part2()
res = 0
for line in test:
    print(line)
    for char in line:
        if char == "O":
            res += 1
print(res)
# up, right, down, left, up...
