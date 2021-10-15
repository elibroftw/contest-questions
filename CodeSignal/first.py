import random

def threeCharsDistinct(s):
    val = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) == 3:
            val += 1
    return val


def sumOfStrings(a, b):
    '''
    Add every ith digit of the first string to the ith digit of the second string,
    both counted from the end. If the ith digit of one of the strings is absent,
    the sum will be the ith digit of the other string. Return a string of those sums concatenated with each other.
    '''
    longest = max(len(a), len(b))
    values = []  # output
    for i in range(1, longest + 1):
        left = 0 if i > len(a) else int(a[-i])
        right = 0 if i > len(b) else int(b[-i])
        values.append(str(left + right))
    return ''.join(reversed(values))


def alignedMemoryAllocator2(memory, queries):
    """
    Untested.
    last was 50%
    """
    results = []
    allocs = {}
    for operation, what in queries:
        if operation == 0:  # alloc
            i = 0
            allocated = False
            while i <= len(memory) - what and not allocated:
                if i % 8 == 0:
                    i += 1
                    continue
                good_to_alloc = True
                # check if units are all free
                for j in range(i, i + what):
                    if memory[j]:
                        i = j + 1
                        good_to_alloc = False
                        break
                if good_to_alloc:
                    # allocate units
                    for j in range(i, i + what):
                        memory[j] = 1
                    allocated = True
            if not allocated:
                results.append(-1)
        elif operation == 1:  # erase
            if what >= len(memory) or memory[what] == 0:
                results.append(-1)
            else:
                results.append(allocs.pop(what, 1))
                # free memory
                for index in range(what, what + results[-1]):
                    memory[index] = 0
    return results


def rectangleBoxes(operations):
    """
    19/20
    """
    biggest_width = None
    biggest_height = None
    largest_rect = None
    # keep track of only widest and longest rectange
    results = []
    for operation in operations:
        if operation[0] == 0:
            if biggest_width is None or biggest_width[0] < operation[1]:
                biggest_width = operation[1:]

            if biggest_height is None or biggest_height[1] < operation[2]:
                biggest_height = operation[1:]

            if largest_rect is None or largest_rect[0] * largest_rect[1] < operation[1] * operation[2]:
                largest_rect = operation[1:]
        elif operation[0] == 1:
            result = True
            for rectangle in (biggest_width, biggest_height, largest_rect):
                if rectangle is not None:
                    a, b = rectangle
                    w = operation[1]
                    h = operation[2]
                    if (a > w or b > h) and (a > h or b > w):
                        result = False
                        break
                # either a <= w && b <= h or a <= h and b <= w to be good
            results.append(result)
    return results


if __name__ == '__main__':
    assert sumOfStrings('99', '99') == '1818'
    assert sumOfStrings('11', '9') == '110'
    string_1 = ''.join(str(random.randint(0, 9)) for _ in range(10 ** 5))
    string_2 = ''.join(str(random.randint(0, 9)) for _ in range(10 ** 5))
    sumOfStrings(string_1, string_2)
    memory = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    queries = [[0, 2], [0, 1], [0, 1], [1, 0], [1, 8], [0, 3], [1, 5], [0, 4]]
    assert alignedMemoryAllocator2(memory, queries) == [8, 0, -1, 1, 2, 8, 1, -1]
    alignedMemoryAllocator2(memory, queries)
    rectangleBoxes([[1,22,20],
                    [1,29,5],
                    [1,18,18],
                    [0,6,6],
                    [0,30,4],
                    [1,9,25],
                    [1,28,12],
                    [0,4,20],
                    [0,17,7],
                    [0,6,6],
                    [0,4,10],
                    [0,26,11],
                    [1,26,15],
                    [1,4,22],
                    [0,4,15]])
