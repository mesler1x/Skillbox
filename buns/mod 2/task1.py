numbers = input()
first = 0
second = 0
sum = 0

for number in numbers:
    if number == ',':
        first = int(numbers[:sum])
        second = int(numbers[sum + 2:])
    sum += 1
print(first % second)