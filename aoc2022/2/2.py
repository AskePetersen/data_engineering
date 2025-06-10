def get_dict():
    dick = {}
    for i, c in enumerate(range(97, 97 + 26)):
        dick[chr(c)] = i + 1
    for i, c in enumerate(range(65, 91)):
        dick[chr(c)] = i + 27
    return dick


def part1(input):
    dick = get_dict()
    lst = input.split("\n")
    res = 0
    for ele in lst:
        halv = len(ele) // 2
        første, anden = ele[:halv], ele[halv:]
        for c in første:
            if c in anden:
                res += dick[c]
                break
    print(res)


file = "input"
with open(file) as f:
    input = f.read().strip()
part1(input)
