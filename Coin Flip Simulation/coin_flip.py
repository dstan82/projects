from random import randint


def coin_flip(number_of_throws):
    heads, tails = 0, 0
    for throw in range(number_of_throws):
        if randint(0, 1) == 1:
            heads += 1
        else:
            tails += 1
    return f'Coin was flipped {number_of_throws} times with {heads} heads and {tails} tails.'


print(coin_flip(int(input('How many times do you want to flip the coin:'))))
