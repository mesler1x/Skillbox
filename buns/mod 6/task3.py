def armstrong_numbers():
    for num in range(10, 10 ** 8):
        power = len(str(num))
        sum_of_digits = sum(int(digit) ** power for digit in str(num))
        if sum_of_digits == num:
            yield num


generator = armstrong_numbers()


def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
