def decode(message, dictionary):
    decoded = ''
    end = 1
    while len(message) > 0:
        part = message[:end]
        if part in dictionary:
            decoded += dictionary[part]
            message = message[end:]
            end = 0
        end += 1
    return decoded


k = int(input())
cool_dictionary = {}
for i in range(k):
    user_input = input().split()
    cool_dictionary[user_input[1]] = user_input[0]
encoded = input()
print(decode(encoded, cool_dictionary))
