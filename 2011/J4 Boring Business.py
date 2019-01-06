path = [(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), (5, -5), (5, -4), (5, -3),
         (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7),
         (0, -7), (-1, -7), (-1, -6), (-1, -5)]

command = ''
in_danger = False
message = 'safe'
while not in_danger:
    user_input = input().split(' ')
    command, units = user_input[0], int(user_input[1])
    new_hole_x, new_hole_y = path[-1]
    if command == 'q': break
    if command in ('d', 'u'):
        if command == 'u':
            positive_direction = 1
        else:
            positive_direction = -1

        for i in range(units):
            new_hole_y = new_hole_y + positive_direction * 1
            if (new_hole_x, new_hole_y) in path:
                in_danger = True
            path.append((new_hole_x, new_hole_y))
    elif command in ('l', 'r'):
        if command == 'r':
            positive_direction = 1
        else:
            positive_direction = -1

        for i in range(units):
            new_hole_x = new_hole_x + positive_direction * 1
            if (new_hole_x, new_hole_y) in path:
                in_danger = True
            path.append((new_hole_x, new_hole_y))
    if in_danger:
        message = 'DANGER'
    print(new_hole_x, new_hole_y, message)
