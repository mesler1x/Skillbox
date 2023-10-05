code = input()
switch = True
sum = 0
for num in code:
    if switch:
        sum += int(num)
        switch = False
    else:
        sum += int(num) * 3
        switch = True