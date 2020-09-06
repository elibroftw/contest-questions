import random
import time
solution = __import__('5825 Non-negative Partial Sums')
solve = solution.solve


assert solve(5, [14, 1, 1, -5, -9]) == 1
assert solve(5, [1, 1, 1, -5, -9]) == 0
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
solve(10 ** 4, [1000 if random.randint(0, 2) else -1000 for _ in range(10 ** 4)])  # 10 ** 4
solve(10 ** 5, [1000 if random.randint(0, 2) else -1000 for _ in range(10 ** 5)])  # 10 ** 5
for x in range(20):
    # length = 10 ** 6
    # simulate string input
    hard_lst = ' '.join([str(random.randint(-1000, 1000)) for _ in range(10 ** 6)])
    t1 = time.time()
    integers = [int(x) for x in hard_lst.split()]
    ans = solve(10 ** 6, integers)
    print(time.time() - t1)
