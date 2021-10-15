from pprint import pprint
def mutateTheArray(n, a):
    # return array b of length n
    b = []
    for i in range(n):
        first = a[i - 1] if i else 0
        last = a[i + 1] if i + 1 < len(a) else 0
        b.append(first + a[i] + last)
    return b


def makeIncreasing(numbers):
    swaps_required = set()

    for i in range(1, len(numbers)):
        num = numbers[i]
        if i < len(numbers) - 1 and num >= numbers[i + 1]:

            if (i - 1) in swaps_required and numbers[i - 1]:
                pass
        elif i > 0 and num <= numbers[i - 1]:
            swaps_required += 1
    return len(swaps_required) <= 1



def get_diagonal(a, i):
    b = []
    r, c = (0, i) if i < len(a) else (i - len(a) + 1, len(a) - 1)
    while r < len(a) and c >= 0:
        b.append(a[r][c])
        r += 1
        c -= 1
    return b



def diagonalsSort(a):
    total_diags = 2 * len(a) - 3
    for i in range(1, total_diags + 1):
        sorted_lst = sorted(get_diagonal(a, i), reverse=True)
        r, c = (0, i) if i < len(a) else (i - len(a) + 1, len(a) - 1)
        i = 0
        while r < len(a) and c >= 0:
            a[r][c] = sorted_lst[i]
            r +=1
            c -= 1
            i += 1
    return a


def preferredRestaurant(preferences):
    num_restuaants = len(preferences[0])
    restaurants = [0 for _ in range(num_restuaants)]

    for preference in preferences:
        for i in range(num_restuaants):
            restaurants[preference[i] - 1] += 10 ** (num_restuaants - i)
    num_maxes = 1
    to_beat = -2
    for i in range(num_restuaants):
        if to_beat < 0 or restaurants[i] > restaurants[to_beat]:
            num_maxes = 1
            to_beat = i
        elif to_beat >= 0 and restaurants[i] == restaurants[to_beat]:
            num_maxes += 1
    print(restaurants)
    if num_maxes > 1:
        to_beat = -2
    return to_beat + 1




if __name__ == '__main__':
    a = [[1, 3, 9, 4],
     [9, 5, 7, 7],
     [3, 6, 9, 7],
     [1, 2, 2, 2]]
    preferences =  [[3,2,1],  [3,2,1],  [3,2,1]]
    preferences = [[3,5,2,6,10,1,7,8,4,9], [8,7,2,4,10,1,5,3,6,9], [7,3,2,10,6,4,1,9,5,8]]
    preferences = [[1,2,3,4,5], [2,3,1,4,5], [4,5,1,3,2]]
    preferredRestaurant(preferences)
    # pprint(diagonalsSort(a))
