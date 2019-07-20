# Keep track of how many rows and columns still need to be merged.
# While there are at least two rows that need to be merged or two columns that need to be merged:
#     Grab the next smallest edge in the graph.
#     If this edge connects two columns which have not yet been merged:
#         Multiply the edge weight by the number of unmerged rows and merge the columns
#     Else, if this edge connects two rows which have not yet been merged:
#         Multiply the edge weight by the number of unmerged columns and merge the rows
# Return the sum of the multiplied edge weights
n, m, p, q = (int(k) for k in input().split())
# n = planets >= 1; rows
# m = cities >= 1; columns
# p = flights per planet
# q = portals (planet1, 2) --> (planet2, 2)
rows = n
columns = m

paths = set()
paths_list = []
energy_saved = 0
total_energy = 0
verticies = n * m
for i in range(p):
    a, b, c = (int(k) for k in input().split())
    # city1, city 2, energy
    path = ((0, a), (0, b), c)
    if a == b or path in paths:
        energy_saved += c * rows
    else:
        paths.add(path)
        total_energy += c * rows

for j in range(1, q + 1):
    x, y, z = (int(k) for k in input().split())
    path = ((x, 0), (y, 0), z)
    if x == y or path in paths:
        energy_saved += z * columns
    else:
        paths.add(path)
        total_energy += z * columns

edges = 0
minimum_energy = 0
safe_rows = {x for x in range(1, rows + 1)}
safe_columns = {y for y in range(1, columns + 1)}

paths_list = sorted(paths, key=lambda path: path[2])
while edges < verticies - 1:
    path = paths_list.pop(0)
    # or use an iterator
    
    # directions = go smallest index to larger index
    energy = path[2]
    if path[0][0] == 0:  # path that connects two columns

        start, end = path[0][1], path[1][1]
        if start > end: start, end = end, start

        if start in safe_columns:
            safe_columns.remove(start)
            columns -= 1
        elif end in safe_columns:
            safe_columns.remove(end)
            columns -= 1
        
        minimum_energy += energy * rows
        edges += rows
        

    else:  # path that connects two rows
        
        start, end = path[0][0], path[1][0]
        if start > end: start, end = end, start

        if start in safe_rows:
            safe_rows.remove(start)
            rows -= 1
        elif end in safe_rows:
            safe_rows.remove(end)
            rows -= 1
        
        minimum_energy += energy * columns
        edges += columns

# SAMPLE INPUT 1
sample_input1 ='''
2 2 1 2
1 2 1
2 1 1
2 1 1
'''
# 3

# SAMPLE INPUT 2
sample_input2 = '''
2 3 4 1
2 3 5
3 2 7
1 2 6
1 1 8
2 1 5
'''
# 41
 
print(total_energy - minimum_energy + energy_saved)


