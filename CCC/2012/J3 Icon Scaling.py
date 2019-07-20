icon = ['*', 'x', '*'], [' ', 'x', 'x'], ['*', ' ', '*']
k = int(input())

for row in icon:
    for _ in range(k):
        for pixel in row:
            print(k * pixel, end='')
        print()
