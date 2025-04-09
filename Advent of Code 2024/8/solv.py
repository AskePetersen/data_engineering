def prev(p1, p2):
    diff_x = p2[0] - p1[0]
    diff_y = p1[1] - p2[1]
    prev_pos = p1[0] - diff_x, p1[1] + diff_y

    return prev_pos


def next(p1, p2):
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]
    next_pos = p2[0] + diff_x, p2[1] + diff_y

    return next_pos


def check_pos(pos):
    return MIN_X <= pos[0] < MAX_X and MIN_Y <= pos[1] < MAX_Y


def prev_posses(p1, p2):
    diff_x = p2[0] - p1[0]
    diff_y = p1[1] - p2[1]
    prev_pos = p1[0] - diff_x, p1[1] + diff_y
    res = []
    prev_prev_pos = p1
    while check_pos(prev_pos):
        res.append(prev_pos)
        tmp = prev_pos
        prev_pos = prev(prev_pos, prev_prev_pos)
        prev_prev_pos = tmp

    return res


def next_posses(p1, p2):
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]
    next_pos = p2[0] + diff_x, p2[1] + diff_y
    res = []
    prev_next_pos = p2

    while check_pos(next_pos):
        res.append(next_pos)
        tmp = next_pos
        next_pos = next(prev_next_pos, next_pos)
        prev_next_pos = tmp

    return res


def part1(lines):
    res_set = set()
    char_pos_dict = {}
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == ".":
                continue
            if char not in char_pos_dict:
                char_pos_dict[char] = [(x, y)]
                continue
            posses = char_pos_dict[char]
            curr_pos = (x, y)
            for pos in posses:
                prev_pos = prev(pos, curr_pos)
                next_pos = next(pos, curr_pos)
                if check_pos(prev_pos):
                    res_set.add(prev_pos)
                if check_pos(next_pos):
                    res_set.add(next_pos)
            char_pos_dict[char].append(curr_pos)

    res = len(res_set)
    print(res)


def part2(lines):
    char_pos_dict = {}
    res_list = []
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == ".":
                continue
            if char not in char_pos_dict:
                char_pos_dict[char] = [(x, y)]
                continue

            posses = char_pos_dict[char]
            curr_pos = (x, y)
            for pos in posses:
                res_list.extend(prev_posses(pos, curr_pos))
                res_list.extend(next_posses(pos, curr_pos))
            char_pos_dict[char].append(curr_pos)

    for values in char_pos_dict.values():
        if len(values) == 1:
            continue
        else:
            res_list.extend(values)
    res = len(set(res_list))
    print(res)


file = "input"
with open(file) as f:
    lines = [ele.strip() for ele in f.readlines()]
MIN_X = 0
MIN_Y = 0
MAX_X = len(lines)
MAX_Y = len(lines[0])

part2(lines)
