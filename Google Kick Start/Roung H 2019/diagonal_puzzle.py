from pprint import pprint
tc = int(input())
for t in range(1, tc + 1):
    ak = {}  # answer key
    # # is black
    # . is white
    n = int(input())
    diags = 2 * n - 1
    looking_for = tuple(tuple('#' for __ in range(n)) for _ in range(n))
    special_1 = tuple(tuple('.' for __ in range(n)) for _ in range(n))
    last_move = False
    start = []
    for _ in range(n): start.append(tuple(input()))
    start = tuple(start)
    visited = {start}
    positions = {start}
    ans = 0
    while not last_move:
        temp_pos = set()
        for pos in positions:
            if pos == looking_for:
                ak[start] = ans
                last_move = True
                break
            elif pos == special_1:
                ak[start] = ans + 2 * n - 1
                last_move = True
                break
            for d in range(1, n + 1):
                to_flip = []
                temp1 = [list(row) for row in pos]
                temp2 = [list(row) for row in pos]
                temp3 = [list(row) for row in pos]
                temp4 = [list(row) for row in pos]
                for i, e in enumerate(range(d - 1, -1, -1)):
                    temp1[i][e] = '.' if temp1[i][e] == '#' else '#'
                    temp3[-(i+1)][e] = '.' if temp3[-(i+1)][e] == '#' else '#'
                    if d != n:
                        temp2[i][-(e + 1)] = '.' if temp2[i][-(e + 1)] == '#' else '#'
                        temp4[-(i+1)][-(e + 1)] = '.' if temp4[-(i+1)][-(e + 1)] == '#' else '#'

                temps = (temp1, temp3) if d == n else (temp1, temp2, temp3, temp4)
                for temp in temps:
                    temp = tuple(tuple(c for c in row) for row in temp)
                    if temp not in visited:
                        visited.add(temp)
                        temp_pos.add(temp)

                del temp1, temp2, temp3, temp4
        positions = temp_pos
        ans += 1
    print('Case #', t, ': ', ak[start], sep='')