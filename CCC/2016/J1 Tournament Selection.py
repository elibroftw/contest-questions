x = 0
for i in range(6):
    if input() == 'W': x += 1
if x > 4: print(1)
elif 2 < x < 5: print(2)
elif 0 < x < 3: print(3)
else: print(-1)