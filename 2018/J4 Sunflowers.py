# N different sunflowers with unique heights
# ordered from smallest to largest
# records heights for N consecutive days
# all flowers grow
# smallest in top left, largest in bottom right
grid = []
n = int(input())
for i in range(n):
    grid.append([int(height) for height in input().split()])
smallest = None
row_n = 0
column = 0
for row_number, row in enumerate(grid):
    temp_min = min(row)
    if smallest is None or temp_min < smallest:
        smallest = temp_min
        row_n = row_number
        column = row.index(smallest)

# print(grid[row_n][column])
# new_grid = grid.copy()
new_grid = [[None for x in range(n)] for y in range(n)]
if row_n == 0 and column > 0:  # rotate 90 clock or 270 counter
    for r in range(n):
        for c in range(n):
            new_grid[n-1-c][r] = grid[r][c]
elif row_n > 0 and column == 0:  # rotate 90 counter or 270 clock
    for r in range(n):
        for c in range(n):
            new_grid[c][n-1-r] = grid[r][c]
elif column > 0 and row_n > 0:  # rotate 180
    for r in range(n):
        for c in range(n):
            new_grid[n-1-r][n-1-c] = grid[r][c]
else:
    new_grid = grid.copy()
for row in new_grid:
    for i, spot in enumerate(row):
        if i < n - 1:
            print(spot, end=' ')
        else: print(spot)
