input_num = int(input())
number1 = int(input_num)
number2 = int(input_num)
digits = "0123456789ABCDEF"

if input_num != int(input_num):
    print("Неверный ввод")
else:
    if input_num <= 0:
        print("Неверный ввод")
    else:
        bin1 = ''
        while input_num > 0:
            bin1 = str(input_num % 2) + bin1
            input_num //= 2
        oct1 = ''
        while number1 > 0:
            oct1 = str(number1 % 8) + oct1
            number1 //= 8
        hex1 = ''
        while number2 > 0:
            hex1 = digits[number2 % 16] + hex1
            number2 //= 16
print(bin1 + ',', oct1 + ',', hex1)

