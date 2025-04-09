import re
def part1(input):
    reg = r"mul\(\d+,\d+\)"
    num_reg = r"\d+"
    res = 0
    for match in re.findall(reg, input):
        a,b = map(int, re.findall(num_reg, match))
        res += a*b
    return res
             
def part2(input):
    dont_split = input.split("don't()")
    lst = [dont_split[0]]
    reg = r"mul\(\d+,\d+\)"
    num_reg = r"\d+"
    for ele in dont_split:
        do_split = ele.split("do()")
        lst.extend(do_split[1:])

    res = 0
    for stri in lst:
        for match in re.findall(reg, stri):
            a,b = map(int, re.findall(num_reg, match))
            res += a*b
    return res


if __name__ == "__main__":
    file = "input"
    with open(file) as f:
        data = f.read()
    print(part2(data))
