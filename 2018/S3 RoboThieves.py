def memoize(f):
    memo = {}

    def helper(a):
        if a in memo:
             return memo[a]
        memo[a] = f(a)
        return memo[a]
    return helper



def memoize_2(f):
    memo = {}

    def helper(a, b):
        if (a, b) in memo:
            return memo[a, b]
        else:
            memo[a, b] = f(a, b)
            return memo[a, b]

    return helper


@memoize
def get_col_cams(col):
    return [i for i, r in enumerate(grid) if r[col] == 'C']

@memoize
def get_row_cams(row):
    return [i for i, c in enumerate(grid[row]) if c == 'C']


@memoize_2
def seen_by_camera(row, col):
    row_cams = get_row_cams(row)
    for row_cam in row_cams:
        if 'W' not in grid[row][row_cam:col] and 'W' not in grid[row][col:row_cam]:
            return True
    col_cams = get_col_cams(col)
    for col_cam in col_cams:
        if col_cam - row > 0:
            cells = [grid[i][col] for i in range(row, col_cam)]
        else:
            cells = [grid[i][col] for i in range(col_cam, row)]
        if 'W' not in cells:
            return True
    return False


def add_or_finish_config(row, col):
    if not seen_by_camera(row, col) and grid[row][col] not in ('W', 'C'):
        answers[(row, col)] = steps
        new_configs.add((row, col))
    visited.add((row, col))


def do_step(vertical, horizontal):
    new_row, new_col = row + vertical, col + horizontal
    cell_value = grid[new_row][new_col]

    if (new_row, new_col) not in visited:
        while cell_value in ('U', 'D', 'L', 'R') and (new_row, new_col) not in visited:
            visited.add((new_row, new_col))
            con_vert, con_horz = directions[cell_value]
            # directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
            new_row, new_col = new_row + con_vert, new_col + con_horz
            cell_value = grid[new_row][new_col]
        if not seen_by_camera(new_row, new_col) and cell_value not in ('W', 'C') and (new_row, new_col) not in visited:
            answers[(new_row, new_col)] = steps
            new_configs.add((new_row, new_col))
            visited.add((new_row, new_col))
            
        # elif cell_value == '.':  # just use else  # cell_value = '.'
        #     add_or_finish_config(new_row, new_col)

    

n, m = (int(x) for x in input().split())
grid = []
exits = ()
answers = {}
for i in range(n):
    row = input()
    try: start = i, row.index('S')
    except ValueError: pass
    for o, x in enumerate(row):
        if x == '.':
            t = (i, o)
            answers[t] = -1
            exits += (t,)
    # Calculate row invaldities if time is still an issue
    grid.append(row)

directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
configs = {start}
steps = 0
visited = set()
if not seen_by_camera(*start):
    while configs:
        steps += 1
        new_configs = set()
        for config in configs:
            row, col = config
            do_step(1, 0)   # down one
            do_step(-1, 0)  # up one
            do_step(0, 1)   # right one
            do_step(0, -1)  # left one
        configs = new_configs.copy()    

for exit in exits:
    print(answers[exit])

# SAMPLE INPUT
# 5 7
# WWWWWWW
# WD.L.RW
# W.WCU.W
# WWW.S.W
# WWWWWWW

# WWWWWWW
# WDWCWRW
# WWWWUWW
# WWW.S.W
# WWWWWWW