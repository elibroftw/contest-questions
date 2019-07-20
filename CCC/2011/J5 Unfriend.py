# not  my own solution

n = int(input())
ways = [1, 1, 1, 1, 1, 1, 1]
for i in range(1, n):
    y = int(input())
    ways[y] = ways[y] * (1 + ways[i])

print(ways[n])
