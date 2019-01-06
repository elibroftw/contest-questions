k = int(input())
message = input()
# S = 3P + K
# chr(65) == A
output = ''
for i, letter in enumerate(message):
    p = i + 1
    s = 3 * p + k
    decoded = ord(letter) - s
    if decoded < 65:
        decoded = 91 + decoded - 65
    output += chr(decoded)
print(output)



