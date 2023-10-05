input_numbers = input().replace(' ', '')
input_numbers = ''.join(sorted(input_numbers))

flag = False

for i in range(len(input_numbers) - 1):
    if input_numbers[i] == input_numbers[i + 1]:
        flag = True
        break

print(flag)
