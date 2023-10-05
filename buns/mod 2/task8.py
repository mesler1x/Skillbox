input=input()
char= input[len(input) - 1:]
string= input[:len(input) - 2]

sum = 0

for i in string:
    if i == char:
        sum += 1
    else:
        break

print(sum)