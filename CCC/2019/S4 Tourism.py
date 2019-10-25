from math import ceil
import sys

sys.setrecursionlimit(6000)


def old_tourism(n, k, attractions):
    combos = [(0, attractions)]  # score_so_far, attractions_left
    if n <= k: return max(attractions)
    else:        
        max_days = ceil(n / k)  # if n = 5, and k = 3, max_days = 2
        for day in range(max_days):  # today
            new_combos = []
            days_left = max_days - day - 1
            scores = set()
            for combo in combos:
                score_so_far, attractions_left = combo
                attr_left = len(attractions_left)
                min_attr = attr_left % k
                if min_attr == 0: min_attr = k
                # min_attr = min(min_attr)
                for i in range(min_attr, min(k, attr_left) + 1):
                    attractions_visited = attractions_left[:i]
                    new_attractions_left = attractions_left[i:]
                    n_attr_left = len(new_attractions_left)
                    # if ceil(n_attr_left / k) <= days_left:
                    # if days_left == 0 and new_attractions_left: continue
                    day_score = max(attractions_visited)
                    new_score = score_so_far + day_score
                    new_combos.append((new_score, new_attractions_left))
                    scores.add(new_score)
                    # if not new_attractions_left: final_scores.add(score_so_far + day_score)
            combos = new_combos.copy()
            # print(combos)
        return max(scores)
        # return max(combos, key=lambda schedule: schedule[0])[0]


findings = {}


# memoize
def memoize(fn):
    global findings    
    def helper(n, k, attractions):
        temp = tuple(attractions)
        if (n, k, temp) not in findings: findings[(n, k, temp)] = fn(n, k, attractions)
        return findings[(n, k, temp)]
    return helper


@memoize
def tourism(n, k, attractions):
    min_attr = n % k
    if n <= k: return max(attractions)
    elif min_attr == 0:
        s = 0
        for i in range(0, n, k): s += max(attractions[i:i + k])
        return s
    else:
        s = 0
        for a in range(min_attr, k + 1):
            t = max(attractions[:a]) + tourism(n - a, k, attractions[a:])
            if t > s: s = t
        return s
        

assert tourism(6, 2, [2, 5, 7, 1, 4, 3]) == 16
findings.clear()
assert tourism(5, 2, [2, 5, 7, 1, 4]) == 16
findings.clear()
assert tourism(5, 3, [2, 5, 7, 1, 4]) == 12 
findings.clear()
assert tourism(1, 5, [1]) == 1
findings.clear()
assert tourism(2, 5, [1, 3]) == 3
findings.clear()
assert tourism(6, 4, [1, 2, 3, 4, 5, 6]) == 10
findings.clear()
assert tourism(6, 4, [4, 5, 6, 1, 2, 3]) == 11
findings.clear()

n, k = (int(x) for x in input().split())
attractions = [int(x) for x in input().split()]
print(tourism(n, k, attractions))
