def part1(input):
    lst = input.split("\n\n")
    res_lst = []
    for gruppe in lst:

        inner_lst = gruppe.split("\n")
        tmp_res = 0
        for num in inner_lst:
            a = int(num)
            tmp_res += a
        res_lst.append(tmp_res)
    sorteret_liste = sorted(res_lst, reverse=True)
    print(sum(sorteret_liste[:3]))


file = "input"
with open(file) as f:
    input = f.read().strip()
part1(input)
