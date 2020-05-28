num = int(input('Enter a number:'))


def collatzRecur(num):
    count = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3+1
        count += 1
    return count


print(collatzRecur(num))

# Alternative method
''''
def collatzRecur(curNum, count=0):
    $This recursively solves the Collatz Conjecture
    if curNum <= 1:  # Base case
        return count
    if curNum % 2 == 0:
        return collatzRecur(curNum / 2, count + 1)
    else:
        return collatzRecur(curNum * 3 + 1, count + 1)


print(collatzRecur(2589))
'''
