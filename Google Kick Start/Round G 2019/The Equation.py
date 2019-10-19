t = int(input())
for case in range(t):
    n, m = [int(x) for x in input().split()]
    sv = None
    bv = None
    n_arr = []
    for x in input().split():
        x = int(x)
        if bv is None or x > bv: bv = x
        n_arr.append(x)
    for k in range(min(10 ** 15, int(max(m, bv) * 1.5)), -2, -1):
        sample_sum = 0
        for a in n_arr:
            sample_sum += a ^ k
            if sample_sum > m: break
        if sample_sum <= m: break
    print('Case #', case + 1, ': ', k, sep='')