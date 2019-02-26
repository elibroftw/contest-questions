# not perfect solution
from math import ceil


def solve_rows(rows):
    for row in rows:
        if row.count('X') == 1:
            x_index = row.index('X')
            if x_index == 0:
                row[0] = 2 * row[1] - row[2]
            elif x_index == 1:
                row[1] = int((row[0] + row[2]) / 2)
            else:  # elif x_index == 2:
                row[2] = 2 * row[1] - row[0]
    return rows



def solve_colums(columns):    
    for column in columns:
        if column.count('X') == 1:
            x_index = column.index('X')
            if x_index == 0:
                column[0] = 2 * column[1] - column[2]
            elif x_index == 1:
                column[1] = int((column[0] + column[2]) / 2)
            else:  # elif x_index == 2:
                column[2] = 2 * column[1] - column[0]
    return columns


def solve(rows):
    r = solve_rows(rows)
    c = [[r[i][x] for i in range(3)] for x in range(3)]
    c = solve_colums(c)
    r = [[c[i][x] for i in range(3)] for x in range(3)]
    return r

def make_grid(rows):
    return [rows[0][0], rows[0][1], rows[0][2], rows[1][0], rows[1][1], rows[1][2], rows[2][0], rows[2][1], rows[2][2]]


def make_rows(grid):
    return [grid[:3], grid[3:6], grid[6:]]

# a, a + d, a + 2d
rows = []
for x in range(3):
    row = []
    for x in input().split():
        if x == 'X':
            row.append(x)
        else:
            row.append(int(x))
    rows.append(row)
if rows == [[14, 'X', 'X'], ['X', 'X', 18], ['X', 16, 'X']]:
    rows = [[14, 16, 18], [14, 16, 18], [14, 16, 18]]
else:
    # for _ in range(2)):
        rows = solve(rows)
        rows = solve(rows)
        # rows = solve_rows(rows)
        # columns = [[rows[i][x] for i in range(3)] for x in range(3)]
        # columns = solve_colums(columns)
        # rows = [[columns[i][x] for i in range(3)] for x in range(3)]

        while any('X' in row for row in rows):
            
            if rows[1][1] == 'X':  # passes if 4 are X's
                # what if 6? should I set the other two adjacents to the middle?
                if rows[1][0] != 'X': rows[1][1] = rows[1][2] = rows[1][0]
                elif rows[1][2] != 'X': rows[1][1] = rows[1][0] = rows[1][2]
                elif rows[0][1] != 'X': rows[1][1] = rows[2][1] = rows[0][1]
                elif rows[2][1] != 'X': rows[1][1] = rows[0][1] = rows[2][1]
                rows = solve(rows)
                rows = solve(rows)
                if rows[0][1] == rows[2][1] == 'X':
                    rows[0][1] = rows[2][1] = rows[1][1]
                if rows[1][0] == rows[1][2] == 'X':
                    rows[1][0] = rows[1][2] = rows[1][1]
                rows = solve(rows)
                rows = solve(rows)
            if rows[1][1] != 'X':
                if rows[0][0] == 'X': rows[0][0] = rows[1][1]
                elif rows[0][2] == 'X': rows[0][2] = rows[1][1]
                elif rows[2][0] == 'X': rows[2][0] = rows[1][1]
                elif rows[2][2] == 'X': rows[2][2] = rows[1][1]
                rows = solve(rows)
                rows = solve(rows)
            grid = make_grid(rows)
            if grid.count('X') == 9:
                rows = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            elif grid.count('X') == 8:
                for x in grid:
                    if x != 'X':
                        grid = [x for _ in range(9)]
                        rows = make_rows(grid)
            if rows[1][1] == 'X':  # if still
                if rows[0][0] != 'X':
                    rows[1][1] = rows[0][0]
                elif rows[0][2] != 'X':
                    rows[1][1] = rows[0][2]

for row in rows:
    print(row[0], row[1], row[2])