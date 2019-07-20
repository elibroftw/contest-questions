# p = pies
# k = number of people
# s = min amount of pies
# s = math.ceil(p/k)
# s = p - k + 1
# a = (p - s) / k


def memoize(f):
    memo = {}

    def helper(x, y, w):
        if (x, y, w) not in memo:
            memo[x, y, w] = f(x, y, w)
        return memo[x, y, w]

    return helper

@memoize
def piday(p, k, w):
    if k == 1 or p == k: return 1
    total = 0
    s = p-k+1
    a = (p-s) / (k-1)
    if s > w: s = w
    while 1 <= a <= s:
        total += piday(p-s, k-1, s)
        s -= 1
        a = (p - s) / (k - 1)
    return total

p = int(input())
k = int(input())
print(piday(p, k, p-k+1))

