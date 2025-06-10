def flatten(t):
    if isinstance(t, list):
        flat_list = []
        for item in t:
            flat_list.extend(flatten(item))
        return flat_list
    else:
        return [t]

def remove_ele_from_lst(ele, lst):
    res = []
    for elem in lst:
        if elem == ele:
            pass
        else:
            res.append(elem)
    return res
            

def find_nearby_tar(input, pos, tar):
    x, y = pos
    if x < 0 or y < 0 or x > len(input)-1 or y > len(input[0])-1:
        return (-1, -1)
    if tar == 9 and int(input[x][y]) == 9:
        return pos
    if int(input[x][y]) == tar:
        left_pos = x,y-1
        right_pos = x,y+1
        up_pos = x-1, y
        down_pos = x+1, y
        tar += 1
        return [find_nearby_tar(input, left_pos, tar),
                    find_nearby_tar(input, right_pos, tar),
                    find_nearby_tar(input, up_pos, tar),
                    find_nearby_tar(input, down_pos, tar)]
    else: 
        return (-1, -1)

def solv1(input):
    res = 0
    for l in range(len(input)):
        for c in range(len(input[0])):
            if input[l][c] == '0':
                pos = (l, c)
                raw = flatten(find_nearby_tar(input, pos, 0))
                reduced = remove_ele_from_lst((-1, -1), raw)
                score = len(reduced)
                res += score
    return res



file = "input"
with open(file) as f:
    lines = [ele.strip() for ele in f.readlines()]

if __name__ == '__main__':
    res = solv1(lines)
    print(res)
