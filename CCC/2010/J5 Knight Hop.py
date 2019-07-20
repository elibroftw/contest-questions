ax, ay = [int(_) for _ in input().split()]
bx, by = [int(_) for _ in input().split()]


# ax, ay, bx, by = 1, 1, 2, 2


def knight(x1, y1, x2, y2):
    if (x1, y1) == (x2, y2):
        return 0
    move_set = 1
    latest_a = [[x1, y1]]
    latest_b = [[x2, y2]]
    visited = [[x1, y1], [x2, y2]]
    knight_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    while True:
        if move_set % 2:
            temp_latest_a = []
            for pos in latest_a:
                for move in knight_moves:
                    temp_x1 = pos[0]
                    temp_y1 = pos[1]
                    temp_x1 += move[0]
                    temp_y1 += move[1]
                    if 0 < temp_x1 < 9 and 0 < temp_y1 < 9:
                        if [temp_x1, temp_y1] in latest_b:
                            return move_set
                        if [temp_x1, temp_y1] not in visited:
                            temp_latest_a.append([temp_x1, temp_y1])
                            visited.append([temp_x1, temp_y1])

            latest_a = temp_latest_a.copy()
        else:
            temp_latest_b = []
            for pos in latest_b:
                for move in knight_moves:
                    temp_x1 = pos[0]
                    temp_y1 = pos[1]
                    temp_x1 += move[0]
                    temp_y1 += move[1]
                    if 0 < temp_x1 < 9 and 0 < temp_y1 < 9:
                        if [temp_x1, temp_y1] in latest_a:
                            return move_set
                        if [temp_x1, temp_y1] not in visited:
                            temp_latest_b.append([temp_x1, temp_y1])
                            visited.append([temp_x1, temp_y1])
                latest_b = temp_latest_b.copy()
        move_set += 1


print(knight(ax, ay, bx, by))
