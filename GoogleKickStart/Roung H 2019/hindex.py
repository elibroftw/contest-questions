from collections import defaultdict

tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    citations = defaultdict(int)
    ans = ''
    prev_h = 0
    for i, a in enumerate(input().split()):
        a = int(a)
        h = prev_h
        for k in range(prev_h + 1, min(n, a) + 1):
            citations[k] += 1
            temp = citations[k]
            if temp > h: h = temp
        ans = ans + ' ' + str(h)
        prev_h = h
    print('Case #', t, ': ', ans, sep='')