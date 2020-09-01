# It's Lovely Weather for a Sleigh Ride Together
# https://brilliant.org/problems/day-4-its-lovely-weather-for-a-sleigh-ride/?ref_id=1555333
# author: Elijah Lopez

# read data
with open('trees.txt') as f:
    tree_coords = eval(f.read())


# my solution
def my_calculate_min_time(tree_coords: list, start: tuple, end: tuple) -> int:
    grid = [[1 for _ in range(70)] for _ in range(70)]
    for coord in tree_coords:
        grid[coord[1] - 1][coord[0] - 1] = 0
    if start == end: return 0
    done = False
    visited = [start]
    routes = [start]
    mins = 0
    while not done:
        mins += 1
        new_routes = []
        choices = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for route in routes:
            for choice in choices:
                try:
                    new_y, new_x = route[0] + choice[0], route[1] + choice[1]
                    if (new_y, new_x) == end: return mins
                    if grid[new_y][new_x] and (new_y, new_x) not in visited:
                        new_routes.append((new_y, new_x))
                        visited.append((new_y, new_x))
                except IndexError: pass
        routes = new_routes.copy()


# OP's solution
def jack_calculate_min_time(grid_block, start, end):
    timer = 0
    store = [start]
    while (end not in store):
        y = store
        store = []
        for a in y:
            movement = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for i in movement:
                if ([a[0] + i[0], a[1] + i[1]] not in grid_block):
                    if (a[0] + i[0] > 0 and a[0] + i[0] <= 70):
                        if (a[1] + i[1] > 0 and a[1] + i[1] <= 70):
                            if ([a[0] + i[0], a[1] + i[1]] not in store):
                                store.append([a[0] + i[0], a[1] + i[1]])
        timer = timer + 1
    return timer


# print(my_calculate_min_time(tree_coords, (3, 64), (61, 6)))
# print(jack_calculate_min_time(tree_coords, [65, 4], [7, 62]))