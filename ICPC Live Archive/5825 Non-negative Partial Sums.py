# https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=530&page=show_problem&problem=3836

import random
import time


def solve_old(n, integers):
    iters = 0
    sums = {}
    valid_keys = set()
    keys_to_ignore = set()
    total_sum = 0
    for i, integer in enumerate(integers):
        # add integers in order
        total_sum += integer
        for k in valid_keys:
            if k not in keys_to_ignore:
                iters += 1
                v = sums[k]
                if v + integer < 0:
                    del sums[k]
                    keys_to_ignore.add(k)
                else: sums[k] += integer
        if integer >= 0:
            valid_keys.add(i)
            sums[i] = integer
    if total_sum < 0: return 0  # short-circuit
    for i, integer in enumerate(integers):
        for k in valid_keys:
            if k != i and k not in keys_to_ignore:
                iters += 1
                v = sums[k]
                if v + integer < 0:
                    del sums[k]
                    keys_to_ignore.add(k)
                else: sums[k] += integer
        if i in valid_keys: valid_keys.remove(i)
    print(iters, 'iters v1')
    return len(sums)


def solve(n, integers):
    iters = 0
    valid_seqs = n
    total_sum = 0
    went_back = {}
    sum_cache = {}  # 'i:j': sum
    for i, integer in enumerate(integers):
        iters += 1
        if integer < 0:
            valid_seqs -= 1
            temp_sum = 0
            for j in range(1, len(integers)):
                iters += 1
                temp_num = integers[i - j]
                temp_sum += temp_num
                if temp_sum + integer >= 0:
                    went_back[i] = ((i - j) + len(integers)) % len(integers)
                    print(went_back[i])
                    break
                if temp_num >= 0: valid_seqs -= 1
        total_sum += integer
        # print(iters)
    # print(valid_seqs)
    # print(total_sum)
    if total_sum < 0: return 0
    # print(iters, 'iters v2')
    return valid_seqs


def solvev2(n, integers):
    iters = 0
    valid_seqs = n
    total_sum = 0
    for i, integer in enumerate(integers):
        iters += 1
        if integer < 0:
            valid_seqs -= 1
            temp_sum = 0
            for j in range(1, len(integers)):
                iters += 1
                temp_num = integers[i - j]
                temp_sum += temp_num
                if temp_sum + integer >= 0: break
                if temp_num >= 0: valid_seqs -= 1
        total_sum += integer
        # print(iters)
    if total_sum < 0: return 0
    print(iters, 'iters v2')
    return valid_seqs


# assert solve(5, [1, 1, 1, -5, -9]) == 0
assert solve_old(5, [14, 1, 1, -5, -9]) == 1
assert solve(5, [14, 1, 1, -5, -9]) == 1
assert solve(3, [2, 2, 1]) == 3
assert solve(3, [3, -3, 1]) == 2
assert solve(3, [-3, 3, 1]) == 1
assert solve(3, [2, 2, 0]) == 3
assert solve(3, [-1, 1, 1]) == 2
assert solve(3, [-1, -2, -5]) == 0
assert solve(1, [-1]) == 0
assert solve(2, [-1, -2]) == 0
assert solve(3, [-1, -2, -5]) == 0
assert solve(3, [0, 0, 0]) == 3
assert solve(3, [0, 0, -1]) == 0
assert solve(1, [0]) == 1
assert solve(3, [10, -5, -5]) == 1
assert solve(3, [9, -5, -5]) == 0
assert solve(4, [9, -5, -5, 1]) == 1
assert solve(4, [9, -5, -6, 1]) == 0
assert solve(4, [1000, -1000, -1000, 1000]) == 1
assert solve(4, [1000, 1000, -1000, -1000]) == 1
assert solve(4, [-1000, 1000, 1000, -1000]) == 1
assert solve(4, [1000, -1000, 1000, -1000]) == 2
assert solve(3, [1000, -1000, 0]) == 2
print('10 ** 4')
solve(10 ** 4, [1000 if random.randint(0, 2) else -1000 for _ in range(10 ** 4)])
print('10 ** 5')
solve(10 ** 5, [1000 if random.randint(0, 2) else -1000 for _ in range(10 ** 5)])
print('10 ** 6')  # max length list # TLE test
solve(10 ** 6, [1000 if random.randint(0, 1) else -1000 for _ in range(10 ** 6)])
print('passed tests')

n = 1
while True:
    n = int(input())
    if not n: break
    integers = [int(x) for x in input().split()]
    print(solve(n, integers))
