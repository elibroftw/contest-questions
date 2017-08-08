normal = input()
x = len(normal)
w = x - 1
y = 0
z = 1
a = 1
b = 1
c = 1
d = 0
e = 1
while b == 1:
    if len(normal) == 1:
        print('1')
        break
    if normal[y:z] != normal[w:x]:
        d = d + 1
        x = len(normal) - d
        w = x - 1
        j = normal[y:x]
    if y > w:
        c += 1
        z, d = c, 0
        y = z - 1
        x = len(normal)
        w = x - 1
    if normal[y:z] == normal[w:x]:
        a = x - y
        i = normal[y:x]
    while normal[y:z] == normal[w:x]:
        y += 1
        z += 1
        x -= 1
        w -= 1
        if y > w:
            if a > e:
                e = a
                if c == len(normal):
                    print(e)
                    b = 2
                    break
        if normal[y:z] != normal[w:x]:
            a = 0
            d += 1
            z = c
            y = z - 1
            x = len(normal) - d
            w = x - 1
            break
    if c == len(normal):
        print(e)
        b = 2
