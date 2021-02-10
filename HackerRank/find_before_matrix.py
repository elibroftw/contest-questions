# untested

def findBeforeMatrix(after):
    rows = len(after)
    columns = len(after[0])

    sum_of = {}

    def sum_rows(i, j):
        if i < 0 or j < 0: return 0
        if (i, j) in sum_of: return sum_of[(i, j)]
        return sum_row(i, j) + sum_rows(i - 1, j)

    def sum_row(row, col):
        if col < 0: return 0
        return after[row][col] + sum_row(row, col - 1)


    for i in range(rows):
        for j in range(columns):
            before_other = sum_rows(i, j) - after[i][j]
            after[i][j] = after[i][j] - before_other
            sum_of[(i, j)] = before_other + after[i][j]
    return after


print(findBeforeMatrix([[2, 1], [5, 4]]))
print(findBeforeMatrix([[1, 2], [3, 4]]))  # [[1, 1], [2, 0]]
