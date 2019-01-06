n = [int(input()) for _ in range(4)]

if n[0] > n[1] > n[2] > n[3]:
    print('Fish Diving')
elif n[0] < n[1] < n[2] < n[3]:
    print('Fish Rising')
elif n[0] == n[1] == n[2] == n[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')
