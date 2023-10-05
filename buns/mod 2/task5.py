numbers = input()
i = 0
n = 0
counter = 0

for number in numbers:
    if number == ',':
        i = str(numbers[:counter])
        n = int(numbers[counter + 2:])
    counter += 1

a_to_num = ord(i)

k_to_num = a_to_num + n

if k_to_num < 97:
    k_to_num = 122 - (96 - k_to_num) % 26
elif k_to_num > 122:
    k_to_num = 96 + (k_to_num - 122) % 26

k = chr(k_to_num)

print(k)