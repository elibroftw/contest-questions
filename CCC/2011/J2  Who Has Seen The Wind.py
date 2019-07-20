h = int(input())  # humidity
M = int(input())  # max hours

touches = False
for i in range(M):
    t = i + 1
    A = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
    if A <= 0:
        touches = True
        print('The balloon first touches ground at hour:')
        print(t)
        break

if not touches:
    print('The balloon does not touch ground in the given time.')
