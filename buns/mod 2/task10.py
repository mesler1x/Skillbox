input = input() + ' '
result = ''

for i in range(len(input)):
    if input[i] == ' ':
        result += input[i - 1]

print(result)
