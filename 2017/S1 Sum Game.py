__author__ = 'Elijah Lopez'
__version__ = 1.0
__created__ = '2017-08-26'
'''
S1 - by Elijah Lopez
version 1.0
'''
j = int(input())
sw = [int(x) for x in input().split()]
sp = [int(x) for x in input().split()]
swtotal, sptotal, k = 0, 0, 0
for i in range(0, j):
    swtotal += sw[i]
    sptotal += sp[i]
    if swtotal == sptotal: k = i+1
print(k)
