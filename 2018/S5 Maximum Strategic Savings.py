# concept: minimum spanning tree
# works but is too slow
n, m, p, q = (int(k) for k in input().split())
# n = planets >= 1
# m = cities >= 1
# p = flights per planet
# q = portals (planet1, 2) --> (planet2, 2)
paths = set()
useful_paths = []
energy_saved = 0
total_energy = 0
verticies = n * m
for i in range(p):
    a, b, c = (int(k) for k in input().split())
    # city1, city 2, energy
    path = ((1, a), (1, b), c)
    if path in paths:
        energy_saved += c * n
    else:
        for k in range(1, n + 1):
            path = ((k, a), (k, b), c)
            paths.add(path)
            useful_paths.append(path)
            total_energy += c

for j in range(1, q + 1):
    x, y, z = (int(k) for k in input().split())
    path = ((x, 1), (y, 1), z)
    if path in paths:
        energy_saved += z * m
    else:
        for k in range(1, m + 1):
            path = ((x, k), (y, k), z)
            paths.add(path)
            useful_paths.append(path)
            total_energy += z


edges = 0
minimum_energy = 0
new_paths = set()
new_verticies = set()
useful_paths = sorted(useful_paths, key=lambda path: path[2])  # sort by energy

tree = {}

recollection = {}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited and vertex in graph:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

while edges < verticies - 1:
    path = useful_paths.pop(0)
    start = path[0]
    end = path[1]
    energy = path[2]
    # print(start, end, find_parent(end), find_parent(start), parent_graph)
    # detect if it makese a cycle using BFS/DFS. 
    if start not in bfs(tree, end):
        # new_paths.add((start, end))
        minimum_energy += energy
        edges += 1
        if start in tree: tree[start].add(end)
        else: tree[start] = {end}
        if end in tree: tree[end].add(start)
        else: tree[end] = {start}

# print()
# print(new_paths)
# print(parent_graph)
print(total_energy - minimum_energy + energy_saved)


# SAMPLE INPUT 1
'''
2 2 1 2
1 2 1
2 1 1
2 1 1
======
3
'''
# SAMPLE INPUT 2
'''
2 3 4 1
2 3 5
3 2 7
1 2 6
1 1 8
2 1 5
========
41
'''
