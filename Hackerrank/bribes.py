# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Worth more points than formingMagicSquare but I found this easier.
#  probably because my mind is not accustomed to preprocessing yet.

# By adding 1 or 2 depending on the position of the person
#  we forget the case where the person has bribed people, but because
#  he was bribed, his net placement is 0
#  Checking whether the person 1 or 2 places before him/her is less than him/her is not sufficient
#   as a person before him/her might have been super greedy
#  Then we'd have to check if anyone behind him/her is less than him/her
#  That would require the min function which is taxing

# Therefore, we should try to work our way backwards from the given queue
#  this way all we have to do is check if the person before him/her is 
#  less (the situation/test case in the previous paragraph would not apply for all persons because
#  There will always be a person less than the last guy.
#  In the case of 6 5 4 3 2 1, our algo would go all the way to 6, and move it > 2 and return 'Too chaotic'

def minimumBribes(q):
    bribes = 0
    lowest_value = n
    i = n - 1
    bribe_dict = {}
    while i >= 0:
        person = q[i]
        if i < n - 1 and q[i + 1] < person:
            q[i] = q[i + 1]
            q[i + 1] = person
            i += 1
            # print(person)
            if person in bribe_dict:
                # print(person)
                bribe_dict[person] += 1
                if bribe_dict[person] > 2: return 'Too chaotic'
            else: bribe_dict[person] = 1
            bribes += 1
        else: i -= 1
    return bribes


'''
MY SAMPLE INPUT
4
5
2 1 5 3 4
10
1 2 3 4 6 7 8 9 10 5
6
1 5 2 6 3 4
10
1 2 3 6 5 7 8 4 9 10
'''


if __name__ == '__main__':
    # MY TESTS
    n = 5
    print(minimumBribes([2, 1, 5, 3, 4]))
    n = 10
    print(minimumBribes([1, 2, 3, 4, 6, 7, 8, 9, 10, 5]))
    n = 6
    print(minimumBribes([1, 5, 2, 6, 3, 4]))