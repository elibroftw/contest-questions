from math import ceil
import sys

sys.setrecursionlimit(6000)


findings = {}
# memoize
def memoize(fn):
    global findings    
    def helper(n, k, attractions):
        temp = attractions
        if (n, k, temp) not in findings: findings[(n, k, temp)] = fn(n, k, attractions)
        return findings[(n, k, temp)]
    return helper


# @memoize
def tourism(n, k, attractions: list):
    # problem
    # maximum score in the fewest days possible
    # score per day is determined by max attraction score of the day
    # k: max attraction visits in a day
    # n: number of attractions
    # attractions: attraction scores
    if n <= k: return max(attractions)
    score = findings.get((n, k), 0)
    if score: return score
    remainder_attrs = n % k
    if remainder_attrs:
        for a in range(remainder_attrs, k + 1):
        # for a in range(k, remainder_attrs - 1, -1):
            remaining = n - a
            if remaining % k == 0:
                temp = max(attractions[:a])
                for i in range(a, n, k):
                    temp += max(attractions[i:i + k])  # todo memoize this computation
            else:
                temp = max(attractions[:a]) + tourism(n - a, k, attractions[a:])
            score = max(temp, score)
            if k == 10 and n == 12: print(score)
    else:
        for i in range(0, n, k):
            score += max(attractions[i:i + k])
    findings[(n, k)] = score
    return findings[(n, k)]


if __name__ == "__main__":
    n, k = (int(x) for x in input().split())
    attractions = [int(x) for x in input().split()]
    print(tourism(n, k, attractions))
