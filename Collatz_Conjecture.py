'''
Collatz Conjecture - Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''

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
