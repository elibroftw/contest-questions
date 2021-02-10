# https://www.hackerrank.com/challenges/magic-square-forming/problem
# The only hard part of this question is figuring out that you need to
#  create/use all possible magic squares and doing so
# Basic math skills required.
# 1. Preprocess or figure out the different ways a magic square can be formed
# From trial and error, you would have figured out the middle square is 5

# my preprocess algo is very ugly, a better way would be to 
# https://www.hackerrank.com/challenges/magic-square-forming/forum/comments/297515

# Another way is below
# You know middle is 5, so at least two spots are based on [1, 5) intersection (5, 9]
# Knowing the values of any three spots in a sqaure will let you calculate all possible squares
# The above is something you would figure out with pen, paper and trial & error.
# Just pick variables a and b, and put a, b on any spot in an example square with 5 in the middle 
# Then you just do some algebra on what the other spots will be based on a, b, and 5.
# Then you create a nested for loop that creates these lists
# You know that the sqaure will be a magic square but now you just need to check if the square
#  will contain all number from 1 to 9
# Sets are very useful for this (A set contains only unique elements)

# p = []
# for a in (1, 2, 3, 4, 6, 7, 8, 9):
#  for b in (1, 2, 3, 4, 6, 7, 8, 9):
#    temp = [a, 20 - a - a - b, -5 + a + b, b, 5, 10 - b, 15 - a - b, -10 + a + a + b, 10 - a]
#    if set(temp) == set(range(1, 10)): p.append(temp)

# To find min cost, we just compare each spot in every MS with the corresponding spot in s
#  and then keep track of the minimum cost.



def create_squares():
    squares = []
    numbers = [1, 2, 3, 4, 6, 7, 8, 9]
    combos = [[1, 9], [2, 8], [3, 7], [4, 6]]
    for combo in combos.copy(): combos.append([combo[1], combo[0]])
    for i in range(8):
        n_copy = numbers.copy()
        num1, num2 = combos[i]
        square = [[0, 0, 0], [num1, 5, num2], [0, 0, 0]]
        n_copy.remove(num1)
        n_copy.remove(num2)
        for j in range(8):
            n_copy2 = n_copy.copy()
            other_1, other_2 = combos[j]
            if other_1 not in n_copy2: continue
            n_copy2.remove(other_1)
            n_copy2.remove(other_2)
            square[0][1] = other_1
            square[2][1] = other_2
            for p in range(4):
                l = n_copy2[p]
                first = 15 - l - other_1
                if first != l and first in n_copy2:
                    second = 15 - num1 - l
                    if second != l and second != first and second in n_copy2:
                        third = 10 - l
                        if third != l and third != second and third != first and third in n_copy2:
                            square[0][0] = l
                            square[0][2] = first
                            square[2][0] = second
                            square[2][2] = third                       
                            if sum(square[1]) == sum(square[2]) == (square[0][2] + 5 + square[2][0]) == 15:        
                                squares.append([row.copy() for row in square])
    return squares


def formingMagicSquare(s):
    squares = create_squares()
    min_cost = 100
    for square in squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(square[i][j] - s[i][j])
        if cost < min_cost: min_cost = cost
    return min_cost

