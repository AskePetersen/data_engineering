from time import sleep


def add_tuples(p, step):
    x, y = tuple(map(sum, zip(p, step)))
    return x, y


def solv1(puzzle_input):
    segments = puzzle_input.split("\n\n")
    dic = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    b = segments[0].split("\n")

    dirs = "".join(segments[1].strip())
    board = []
    for y, l in enumerate(b):
        board.append(list(l))
        for x, c in enumerate(l):
            if c == "@":
                p = (x, y)
                break
    for d in dirs:

        if d == "\n":
            continue
        step = dic[d]
        x, y = add_tuples(p, step)
        hit_O = False
        while board[y][x] != "#":
            if board[y][x] == ".":
                board[p[1]][p[0]] = "."
                p = add_tuples(p, step)
                board[p[1]][p[0]] = "@"
                if hit_O:
                    board[y][x] = "O"
                break
            elif board[y][x] == "O":
                hit_O = True
                x, y = add_tuples((x, y), step)
    res = 0
    for l in range(len(board)):
        for c in range(len(board[0])):
            if board[l][c] == "O":
                res += l * 100 + c
    print(res)


if __name__ == "__main__":
    file = "input"
    with open(file) as f:
        puzzle_input = f.read()
    solv1(puzzle_input)
