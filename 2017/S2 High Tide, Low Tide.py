__author__ = 'Elijah Lopez'
__version__ = 1.0
__created__ = '2017-08-26'
'''
S2 High Tide, Low Tide - by Elijah Lopez
version 1.0
'''

n = int(input())
m = [int(x) for x in input().split()]  # m stands for measurements
m.sort()
if n % 2 == 0: tempn = int(n/2)
else: tempn = int((n+1)/2)
lows = m[:tempn][::-1]
highs = m[tempn:]
for i in range(tempn):
    print(lows[i], end=' ')
    if i == tempn-1 and n % 2 == 1:
        pass
    else: print(highs[i], end=' ')

