a, b, c, d, s = (int(input()) for x in range(5))

nikky_steps = [1] * a + [0] * b
length_1 = len(nikky_steps)
byron_steps = [1] * c + [0] * d
length_2 = len(byron_steps)
nikky = 0
byron = 0
for x in range(s):
    nikky += nikky_steps[x % length_1]
    byron += byron_steps[x % length_2]

if nikky > byron:
    print('Nikky')
elif nikky < byron:
    print('Byron')
else:
    print('Tied')
