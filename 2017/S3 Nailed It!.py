def boards_at_height(h):
    global boards, temp
    x = max(1, h-2000)
    y = h - x
    num_of_boards = 0
    while x <= h//2:
        if x == y:
            try:
                used_boards = values[x] // 2
                temp[x] -= used_boards * 2
                num_of_boards += used_boards
            except KeyError: pass

        else:
            try:
                used_boards = min(values[x], temp[y])
                temp[x] -= used_boards
                temp[y] -= used_boards
                num_of_boards += used_boards
            except KeyError: pass
        x += 1
        y -= 1
    return num_of_boards
n = input()
boards = [int(x) for x in input().split()]
values = {}
for x in boards:
    if x in values: values[x] += 1
    else:
        values[x] = 1
length = 0
ways = 0
for i in range(2, 4001):
    temp = values.copy()
    b = boards_at_height(i)
    if b > length:
        length, ways = b, 0
    if b == length:
        ways += 1
print(length, ways)
