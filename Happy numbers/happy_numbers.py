def is_happy_number(number):
    test_list = []
    while True:
        square = 0
        for digit in str(number):
            square += int(digit)**2
        if square in test_list:
            return False
        elif square == 1:
            return True
        else:
            test_list.append(square)
        number = square


def count_happy_numbers(provided_number):
    happy_numbers = []
    while len(happy_numbers) < 8:
        if is_happy_number(provided_number):
            happy_numbers.append(provided_number)
        provided_number += 1
    return happy_numbers


print(count_happy_numbers(int(input('Provide a number:'))))
