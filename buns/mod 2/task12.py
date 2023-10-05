input_phone = input()
incorrect = "-() "
phone = ""

for num in input_phone:
    if not(num in incorrect):
        phone += num

print(phone)
