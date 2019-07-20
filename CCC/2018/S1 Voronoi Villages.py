n = int(input())
villages = []
for i in range(n):
    villages.append(int(input()))
villages.sort()
min_size = 2000000001
for i, x in enumerate(villages):
    if n - 1 > i > 0:
        before = villages[i - 1]
        after = villages[i + 1]
        size = (x - before) / 2 + (after - x) / 2
        if size < min_size:
            min_size = size
print(min_size)
