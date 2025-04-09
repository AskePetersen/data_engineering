def part1():
    file = "input"
    with open(file) as f:
        data = f.read().strip().split("\n")

    x, y = 0, 0
    arrs = []
    for i, line in enumerate(data):
        arrs.append(list(line))

        for j, char in enumerate(line):
            if char == "^":
                x, y = i, j

    while True:
        while arrs[x][y] != "#":
            arrs[x][y] = "1"
            x = x - 1
            if x < 0:
                return arrs
        x = x + 1
        while arrs[x][y] != "#":
            arrs[x][y] = "1"
            y = y + 1
            if y >= len(arrs[0]):
                return arrs
        y = y - 1
        while arrs[x][y] != "#":
            arrs[x][y] = "1"
            x = x + 1
            if x >= len(arrs):
                return arrs
        x = x - 1
        while arrs[x][y] != "#":
            arrs[x][y] = "1"
            y = y - 1
            if y < 0:
                return arrs
        y = y + 1


arrs = part1()
res = 0
for arr in arrs:
    for char in arr:
        if char == "1":
            res += 1
print(res)
# up, right, down, left, up...
