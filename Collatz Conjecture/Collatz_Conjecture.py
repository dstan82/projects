num = int(input('Enter a number:'))


def collatz(num):
    count = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3+1
        count += 1
    return count


print(collatz(num))

''''
def collatz(current_number, count=0):
    if current_number <= 1:
        return count
    if current_number % 2 == 0:
        return collatz(current_number / 2, count + 1)
    else:
        return collatz(current_number * 3 + 1, count + 1)


print(collatz(num))
'''
