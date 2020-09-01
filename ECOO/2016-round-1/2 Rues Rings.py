def read_data(filename='DATA/DATA20.txt'):
    with open(filename) as f:
        data = f.read().splitlines()
    better_data = []
    start = n = 0
    for i, v in enumerate(data):
        if i == start:
            n = int(v)
        elif i == start + n:
            better_data.append(data[start + 1:start + n + 1])
            start = i + 1
    return better_data


def find_problems(routes):
    min_dia = 70001
    output = []
    for route in routes:
        route = [int(x) for x in route.split(' ')]
        route_min = min(route[2:])
        if route_min < min_dia:
            min_dia = route_min
    for route in routes:
        route = [int(x) for x in route.split(' ')]
        if route[2:].count(min_dia):
            output.append(route[0])
    print(min_dia, end=' {')
    for i, v in enumerate(output):
        if i > 0:
            print(',', v, end='', sep='')
        else:
            print(v, end='')
    print('}')


places = read_data()
for place in places:
    find_problems(place)
