# n = int(input())
# boards = [int(x) for x in input().split()]
# boards.sort()
# maxlength, hlist, tmp, hlist, output = 1 + n // 2, [], boards.copy(), [], 0
# for i in range(0, n): #1, 1, 1, 3
#     tmp.pop(0)
#     for num in tmp:
#         if boards[i] == num and boards.count(boards[i]) // 2 > hlist.count(boards[i] + num) or tmp.count(
#                 boards[i]) == 0:
#             hlist.append(boards[i] + num)
#
# hlist.sort()
# while output == 0:
#     tmp, maxlength = 'FILLER', maxlength - 1
#     for heights in hlist:
#         if heights == tmp: continue
#         if hlist.count(heights) >= maxlength: output += 1
#         tmp = heights
# print(maxlength, output)
n = int(input())
boards = [int(x) for x in input().split()]
boards.sort()
maxlength, hlist, tmp, hlist, output = 0, [], boards.copy(), [], 0
for i in range(0, n): #1, 1, 1, 3
    tmp.pop(0)
    for num in tmp:
        if boards[i] == num and boards.count(boards[i]) // 2 > hlist.count(boards[i] + num) or tmp.count(
                boards[i]) == 0:
            hlist.append(boards[i] + num)
            if hlist.count(hlist[-1]) > maxlength:
                maxlength, output = hlist.count(hlist[-1]), 1
            elif hlist.count(hlist[-1]) == maxlength: output += 1
print(maxlength, output)