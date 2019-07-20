q = int(input())
n = int(input())
i = 0
a = ([int(x) for x in input().split()])
b = ([int(x) for x in input().split()])
if q == 1:
    for j in range(0, n):
        if not a: break
        A, aa, B, bb = max(a), min(a), max(b), min(b)
        i += max(A, B)
        a.remove(A)
        b.remove(bb)
        if not a: break
        i += max(aa, bb)
        a.remove(aa)
        b.remove(B)
if q == 2:
    for j in range(0, n):
        if not a: break
        A, aa, B, bb = max(a), min(a), max(b), min(b)
        i = i + max(A, bb)
        a.remove(A)
        b.remove(bb)
        if not a: break
        i += max(aa, B)
        a.remove(aa)
        b.remove(B)
print(i)
