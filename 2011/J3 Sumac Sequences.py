t1 = int(input())
t2 = int(input())
terms = [t1]
latest_term = t2
length = 1
while latest_term >= 0:
    terms.append(latest_term)
    length += 1
    latest_term = terms[length - 2] - terms[length - 1]

print(length)
