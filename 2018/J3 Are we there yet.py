# 5 Cities
# 4 numbers
cities = [0]
cities.extend([int(city) for city in input().split()])
# print(cities[0:5])
# 1...2...3...4...5
# 0   3   10  12  5

# 0   3   13  25  30
for i in range(5):
    ref = cities[i]
    to_print = str(sum(cities[0:i+1]))
    for j in range(1, 5):
        if i > j:
            to_print += ' ' + str(sum(cities[j+1:i+1]))
        else:
            to_print += ' ' + str(sum(cities[i+1:j+1]))
    print(to_print)
