def part1():
    file = "input"

    with open(file) as f:
        data = f.read().strip()
    free_space = False
    my_str = ""
    curr_val = 0
    for char in data:

        curr_int = int(char)
        if not free_space:
            my_str += str(curr_val) * curr_int
            curr_val += 1
        else:
            my_str += "." * curr_int

        free_space = not free_space

    res_str = ["." for _ in my_str]
    dot_count = my_str.count(".")
    end = len(my_str) - dot_count
    res_str_idx = 0
    for i in range(end):
        # if i == 12:
        #     breakpoint()
        if my_str[i] != ".":
            res_str[i] = my_str[i]
        else:
            while my_str[-res_str_idx - 1] == ".":
                res_str_idx += 1
            res_str[i] = my_str[-res_str_idx - 1]
            res_str_idx += 1
    res = "".join(res_str)
    checksum = 0
    i = 0
    while True:
        if res[i] == ".":
            break
        checksum += i * int(res[i])
        i += 1
    print(f"{checksum}")


part1()
# res='0099811188827773336446555566..............'
# res='0099811188827773336446555566..............'
