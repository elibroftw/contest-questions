def read_data(filename='DATA/DATA11.txt'):
    with open(filename) as f:
        data = f.read().splitlines()
    return data


def calculate_delay(data):
    start = 0
    t = n = 0
    busy_until = 0
    for i in range(len(data)):
        if i == start:
            t, n = (int(x) for x in data[i].split(' '))
        else:
            event = data[i]
            if event == 'B':
                if busy_until < i - start:
                    busy_until = i - start + t - 1
                else:
                    busy_until = busy_until + t
        if i == start + n:
            if busy_until - n > 0:
                print(busy_until - n)
            else:
                print(0)
            start = i + 1
            busy_until = 0


calculate_delay(read_data())
calculate_delay(read_data('DATA/DATA10.txt'))
# calculate_delay(['3 5', 'E', 'B', 'E', 'B', 'E', '2 4', 'B', 'E', 'E', 'E'])
