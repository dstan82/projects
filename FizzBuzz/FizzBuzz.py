def FizzBuzz():
    my_list = [num for num in range(101)]
    fizz_buzz_list = []
    for num in my_list[1:]:
        if num % 3 == 0 and num % 5 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif num % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif num % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(num)
    return fizz_buzz_list


print(FizzBuzz())
