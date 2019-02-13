# movements are down or right
# brother in (R,C)
# find number of paths to (R, C) if you cannot go between cats
# 1, 1 is top left
r, c = (int(x) for x in input().split(' '))
k = int(input())
cats = []
for _ in range(k):
    x, y = (int(x) for x in input().split(' '))
    cats.append((x - 1, y - 1))


def memoize(f):
    memo = {}

    def helper(a, b):
        if (a, b) in memo:
            return memo[a, b]
        else:
            memo[(a, b)] = f(a, b)
            return memo[a, b]

    return helper


@memoize
def ways(x, y):
    if x == 0 and y == 0:
        return 1
    elif (x, y) in cats:
        return 0
    if x == 0:
        return ways(x, y - 1)
    elif y == 0:
        return ways(x - 1, y)
    return ways(x - 1, y) + ways(x, y - 1)


if r == c == 1:
    print(0)
else:
    print(ways(r - 1, c - 1))