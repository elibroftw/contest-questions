i = [int(x) for x in input().split()]
ii = [int(x) for x in input().split()]
iii = [int(x) for x in input().split()]
iv = [int(x) for x in input().split()]
x = sum(i)
if (x == sum(ii) and x == sum(iii) and x == sum(iv)
    and x == (i[0] + ii[0] + iii[0] + iv[0]) and x == (i[1] + ii[1] + iii[1] + iv[1])
        and x == (i[2] + ii[2] + iii[2] + iv[2])): print('magic')
else: print('not magic')
