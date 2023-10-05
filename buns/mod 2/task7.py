result = input()
sum1 = 0
sum2 = 0

for char in result:
    if char == "0":
        sum1 += 1
    elif char == "1":
        sum2 += 1

if sum1 == sum2:
    print("yes")
else:
    print("no")


