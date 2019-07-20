# N parking spaces
# Yesterday recorded which parking spaces are empty and occupied
# same info recorded today
# how many are still ocupied
n = int(input())
day1 = input()
day2 = input()
counter = 0
for i in range(n):
    if day1[i] == day2[i] == 'C': counter += 1
print(counter)
